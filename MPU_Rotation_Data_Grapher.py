import pandas as pd
from pandas_datareader import data, wb
import plotly.graph_objs as go

df = pd.read_csv('AlphaComp_0.csv')

fig = go.Figure()

fig.add_trace(go.Scatter(x=df['time'], y=df['roll'], name='ROLL'))
fig.add_trace(go.Scatter(x=df['time'], y=df['pitch'], name='PITCH'))
fig.update_xaxes(rangeslider_visible=True)

fig.update_layout(
    title="MPU6050 - ROLL, PITCH & YAW",
    xaxis_title="TIME (SECONDS)",
    yaxis_title="DEGREES",
    legend_title="ROTATION TYPE"
)

fig.show()