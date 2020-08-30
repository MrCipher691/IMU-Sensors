import matplotlib.pyplot as plt
import csv

x=[]
yaccx=[]
yaccy=[]
yaccz=[]
ygyrox=[]
ygyroy=[]
ygyroz=[]

with open('MPURawData_0.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        yaccx.append(float(row[1]))
        yaccy.append(float(row[2]))
        yaccz.append(float(row[3]))
        ygyrox.append(float(row[4]))
        ygyroy.append(float(row[5]))
        ygyroz.append(float(row[6]))

fig, axs = plt.subplots(2, 3)
fig.suptitle('MPU-6050 RAW DATA')

axs[0, 0].plot(x, yaccx, 'tab:red')
axs[0, 0].set_title('Accel: X-Axis')

axs[0, 1].plot(x, yaccy, 'tab:green')
axs[0, 1].set_title('Accel: Y-Axis')

axs[0, 2].plot(x, yaccz, 'tab:blue')
axs[0, 2].set_title('Accel: Z-Axis')

axs[1, 0].plot(x, ygyrox, 'tab:red')
axs[1, 0].set_title('Gyro: X-Axis')

axs[1, 1].plot(x, ygyroy, 'tab:green')
axs[1, 1].set_title('Gyro: X-Axis')

axs[1, 2].plot(x, ygyroz, 'tab:blue')
axs[1, 2].set_title('Gyro: X-Axis')

for ax in axs.flat:
    ax.set(xlabel = 'Time-(s)')
    ax.label_outer()

plt.show()