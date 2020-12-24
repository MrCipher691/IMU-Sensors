import pandas as pd
from pandas_datareader import data, wb
import plotly.graph_objs as go

df = pd.read_csv(r'MPURawData_0.csv')

fig = go.Figure()

fig.add_trace(go.Scatter(x=df['time'], y=df['acceleration x'], name='ACCEL X'))
fig.add_trace(go.Scatter(x=df['time'], y=df['acceleration y'], name='ACCEL Y'))
fig.add_trace(go.Scatter(x=df['time'], y=df['acceleration z'], name='ACCEL Z'))
fig.add_trace(go.Scatter(x=df['time'], y=df['gyroscope x'], name='GYRO X'))
fig.add_trace(go.Scatter(x=df['time'], y=df['gyroscope y'], name='GYRO Y'))
fig.add_trace(go.Scatter(x=df['time'], y=df['gyroscope z'], name='GYRO Z'))
fig.update_xaxes(rangeslider_visible=True)

fig.update_layout(
    title="MPU6050 - RAW DATA",
    xaxis_title="TIME",
    yaxis_title="g & g/s",
    legend_title="DATA TYPE"
)

fig.show()