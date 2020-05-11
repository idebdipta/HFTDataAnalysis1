
import plotly.graph_objects as go

import pandas as pd


df = pd.read_csv('FT.csv')

fig = go.Figure(data=go.Ohlc(x=df['Time'],
                open=df['O'],
                high=df['H'],
                low=df['L'],
                close=df['C']))
fig.update(layout_xaxis_rangeslider_visible=False)
fig.show()