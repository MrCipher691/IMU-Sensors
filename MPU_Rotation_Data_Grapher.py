import matplotlib.pyplot as plt
import pandas as pd

df_mpu = pd.read_csv(r'MPURotationData_0.csv')
df_alp = pd.read_csv(r'AlphaComp_2.csv')

ax = plt.gca()

df_mpu.plot(kind='line', x='time', y='pitch',color='red', ax=ax)
df_alp.plot(kind='line', x='newTime', y='pitch',color='orange', ax=ax)
plt.show()