import matplotlib.pyplot as plt
import pandas as pd

df_mpu = pd.read_csv(r'MPURawData_0.csv')

ax = plt.gca()

df_mpu.plot(kind='line', x='time', y='acceleration x',color='red', ax=ax)
df_mpu.plot(kind='line', x='time', y='acceleration y',color='orange', ax=ax)
df_mpu.plot(kind='line', x='time', y='acceleration z',color='yellow', ax=ax)
df_mpu.plot(kind='line', x='time', y='gyroscope x',color='blue', ax=ax)
df_mpu.plot(kind='line', x='time', y='gyroscope y',color='purple', ax=ax)
df_mpu.plot(kind='line', x='time', y='gyroscope z',color='black', ax=ax)

plt.show()