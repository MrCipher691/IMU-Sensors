import matplotlib.pyplot as plt
import csv

time = []
xdegree = []
ydegree = []
zdegree = []

with open('MPURotationData_0.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        time.append(float(row[0]))
        xdegree.append(float(row[1]))
        ydegree.append(float(row[2]))
        zdegree.append(float(row[3]))

fig, axs = plt.subplots(2, 2)
fig.suptitle('MPU-6050 ROLL, PITCH & YAW')

axs[0,0].plot(time, xdegree, 'tab:red')
axs[0, 0].set_title('Roll - X Axis')

axs[0,1].plot(time, ydegree, 'tab:green')
axs[0, 1].set_title('Pitch - Y Axis')

axs[1,0].plot(time, zdegree, 'tab:blue')
axs[1, 0].set_title('Yaw - Z Axis')

axs[1,1].plot(time, xdegree, 'tab:red')
axs[1,1].plot(time, ydegree, 'tab:green')
axs[1,1].plot(time, zdegree, 'tab:blue')
axs[1, 1].set_title('Combined - X Y Z Axis')

for ax in axs.flat:
    ax.set(xlabel = 'Time - (s)', ylabel = 'Degrees')
    ax.label_outer()

plt.show()