import matplotlib.pyplot as plt
import pandas as pd

df_mpu = pd.read_csv(r'MPURotationData_0.csv')
df_alp = pd.read_csv(r'AlphaComp_0.csv')

ax = plt.gca()

df_mpu.plot(kind='line', x='time', y='roll',color='red', ax=ax)
df_alp.plot(kind='line', x='time', y='roll',color='orange', ax=ax)
plt.show()