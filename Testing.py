import matplotlib.pyplot as plt
import pandas as pd

f = open('newfile.csv', 'w+')
f.write("time,acceleration x, acceleration x, acceleration z, gyroscope x, gyroscope y, gyroscope z")
f.write("\r\n")

df_mpu = pd.read_csv(r'MPURawData_0.csv')
time = df_mpu['time']
accelx = df_mpu['acceleration x']
accely = df_mpu['acceleration y']
accelz = df_mpu['acceleration z']
gyrox = df_mpu['gyroscope x']
gyroy = df_mpu['gyroscope y']
gyroz = df_mpu['gyroscope z']

new_time = []
new_accelx = []
new_accely = []
new_accelz = []
new_gyrox = []
new_gyroy = []
new_gyroz = []

for i in range(1, len(accelx)+1, 3):
    new_time.append((time[i-1]+time[i]+time[i+1])/3)
    new_accelx.append((accelx[i-1]+accelx[i]+accelx[i+1])/3)
    new_accely.append((accely[i-1]+accely[i]+accely[i+1])/3)
    new_accelz.append((accelz[i-1]+accelz[i]+accelz[i+1])/3)
    new_gyrox.append((gyrox[i-1]+gyrox[i]+gyrox[i+1])/3)
    new_gyroy.append((gyroy[i-1]+gyroy[i]+gyroy[i+1])/3)
    new_gyroz.append((gyroz[i-1]+gyroz[i]+gyroz[i+1])/3)

for i in range(408):
    f.write("{:.4},{:.4},{:.4},{:.4},{:.4},{:.4},{:.4}".format(new_time[i], new_accelx[i], new_accely[i], new_accelz[i], new_gyrox[i], new_gyroy[i], new_gyroz[i]))
    f.write("\r\n")

plt.plot(time, accelx, color='red', marker='o', linestyle='None')
plt.plot(time, accely, color='blue', marker='o', linestyle='None')
plt.plot(time, accelz, color='green', marker='o', linestyle='None')
plt.plot(new_time, new_accelx, color='yellow', marker='o', linestyle='dashed')
plt.plot(new_time, new_accely, color='purple', marker='o', linestyle='dashed')
plt.plot(new_time, new_accelz, color='brown', marker='o', linestyle='dashed')
plt.show()