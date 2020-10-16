import pandas as pd
import math

f = open('pureaccel.csv', 'w+')
f.write("time,roll,pitch,yaw")
f.write("\r\n")

df_data = pd.read_csv(r'MPURawData_0.csv')

timestamp = df_data['time'].values.tolist()
ax = df_data['acceleration x'].values.tolist()
ay = df_data['acceleration y'].values.tolist()
az = df_data['acceleration z'].values.tolist()
gyro_scaled_x = df_data['gyroscope x'].values.tolist()
gyro_scaled_y = df_data['gyroscope y'].values.tolist()
gyro_scaled_z = df_data['gyroscope z'].values.tolist()

CONVERSIONG = 3.9

ranger = int(len(timestamp)/2)

for x in range(ranger):
    accelerationX = (ax[x] * CONVERSIONG)
    accelerationY = (ay[x] * CONVERSIONG)
    accelerationZ = (az[x] * CONVERSIONG)
    pitch = 180 * math.atan(accelerationX/math.sqrt(accelerationY*accelerationY + accelerationZ*accelerationZ))/3.14159
    roll = 180 * math.atan(accelerationY/math.sqrt(accelerationX*accelerationX + accelerationZ*accelerationZ))/3.14159
    yaw = 180 * math.atan(accelerationZ/math.sqrt(accelerationX*accelerationX + accelerationZ*accelerationZ))/3.14159
    print('TIME = {:.4}\tROLL = {:.4}\tPITCH={:.4}\tYAW={:.4}'.format(timestamp[x], roll, pitch, yaw))
    f.write('{:.4f}, {:.4f}, {:.4f}, {:.4f}'.format(timestamp[x], roll, pitch, yaw))
    f.write('\r\n')