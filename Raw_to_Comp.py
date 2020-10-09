import math
import os
import time
import csv
import pandas as pd

def file_name_checker(name):
    existing_files = os.listdir("/home/pi/wwr")
    concluder = 0
    for items in existing_files:
        if items == name:
            concluder += 1
        else:
            concluder += 0
    return concluder

def file_renamer(name):
    name = name.split('.')[0]
    number = int(name.split('_')[1])
    name = name.split('_')[0]
    return (name + '_' + str(number + 1) + '.csv')

def the_negotiator(name, number):
    if number == 1:
        name = file_renamer(name)
        number = file_name_checker(name)
        return the_negotiator(name, number)
    if number == 0:
        return name

file_name = str("AlphaComp_0.csv")

#checker = file_name_checker(file_name)
#file_name = the_negotiator(file_name,checker)
f = open(file_name, 'w+')
f.write("time,roll,pitch,yaw")
f.write("\r\n")

print("Data is being logged in: " + file_name)

df_data = pd.read_csv(r'MPURawData_0.csv')

timestamp = df_data['time'].values.tolist()
accel_scaled_x = df_data['acceleration x'].values.tolist()
accel_scaled_y = df_data['acceleration y'].values.tolist()
accel_scaled_z = df_data['acceleration z'].values.tolist()
gyro_scaled_x = df_data['gyroscope x'].values.tolist()
gyro_scaled_y = df_data['gyroscope y'].values.tolist()
gyro_scaled_z = df_data['gyroscope z'].values.tolist()
    
def twos_compliment(val):
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a, b):
    return math.sqrt((a * a) + (b * b))

def get_z_rotation(x,y,z):
    radians = math.atan2(dist(x,y), z)
    return math.degrees(radians)

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

K = 0.98
K1 = 1 - K

time_diff = 0.01

last_x = get_x_rotation(accel_scaled_x[0], accel_scaled_y[0], accel_scaled_z[0])
last_y = get_y_rotation(accel_scaled_x[0], accel_scaled_y[0], accel_scaled_z[0])
last_z = get_z_rotation(accel_scaled_x[0], accel_scaled_y[0], accel_scaled_z[0])

gyro_offset_x = gyro_scaled_x[0] 
gyro_offset_y = gyro_scaled_y[0] 
gyro_offset_z = gyro_scaled_z[0]

gyro_total_x = (last_x) - gyro_offset_x
gyro_total_y = (last_y) - gyro_offset_y
gyro_total_z = (last_z) - gyro_offset_z

#print ("{0:.4f} {1:.2f} {2:.2f} {3:.2f} {4:.2f} {5:.2f} {6:.2f} {7:.2f} {8:.2f}".format( time.time() - now, (last_x), gyro_total_x, (last_x), (last_y), gyro_total_y, (last_y), (last_z), gyro_total_z))

x = 1
limit = int(len(timestamp))
while ( x < limit):

    time.sleep(time_diff - 0.005)
    
    gyro_scaled_x[x] -= gyro_offset_x
    gyro_scaled_y[x] -= gyro_offset_y
    gyro_scaled_z[x] -= gyro_offset_z
    
    gyro_x_delta = (gyro_scaled_x[x] * time_diff)
    gyro_y_delta = (gyro_scaled_y[x] * time_diff)
    gyro_z_delta = (gyro_scaled_z[x] * time_diff)

    gyro_total_x += gyro_x_delta
    gyro_total_y += gyro_y_delta
    gyro_total_z += gyro_z_delta

    rotation_x = get_x_rotation(accel_scaled_x[x], accel_scaled_y[x], accel_scaled_z[x])
    rotation_y = get_y_rotation(accel_scaled_x[x], accel_scaled_y[x], accel_scaled_z[x])
    rotation_z = get_z_rotation(accel_scaled_x[x], accel_scaled_y[x], accel_scaled_z[x])

    last_x = K * (last_x + gyro_x_delta) + (K1 * rotation_x)
    last_y = K * (last_y + gyro_y_delta) + (K1 * rotation_y)
    last_z = K * (last_z + gyro_z_delta) + (K1 * rotation_z)

    instant_time = float(timestamp[x])
    x_rotation = float(rotation_x)
    y_rotation = float(rotation_y)
    z_rotation = float(rotation_z)

    print ("{:.4f} {:.2f} {:.2f} {:.2f}".format(instant_time, (rotation_x), (rotation_y), (rotation_z)))
    
    f.write("{:.4f},{:.4f},{:.4f},{:.4f}".format(instant_time, x_rotation, y_rotation, z_rotation))
    f.write("\r\n")

    instant_time = x_rotation = y_rotation = z_rotation = 0
    x += 1