import matplotlib.pyplot as plt
import pandas as pd

df_mpu = pd.read_csv(r'MPURotationData_0.csv')

ax = plt.gca()

df_mpu.plot(kind='line', x='time', y='roll',color='red', ax=ax)
df_mpu.plot(kind='line', x='time', y='pitch',color='orange', ax=ax)
plt.show()