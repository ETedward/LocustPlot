import os
import pandas as pd


CSV_Path = os.path.join('swarmfreq.csv')
df = pd.read_csv(CSV_Path, nrows=500, skiprows = 110, index_col=0, usecols=[0,1], names = ["date", "frequency"])

CSV_Path2 = os.path.join('hopperfreq.csv')
df2 = pd.read_csv(CSV_Path2, nrows=500, skiprows = 110, index_col=0, usecols=[0,1], names = ["date", "frequency"])

df["datetime"] = df.index
df2["datetime"] = df.index

print(df)
print(df2)
import plotly.graph_objs as go
import plotly.offline as offline

cl1 = df["datetime"].tolist()
cl2 = df["frequency"].tolist()
cl3 = df2["frequency"].tolist()

trace1 = go.Bar(
    x=cl1,
    y=cl3,
    name='Hoppers'
)

trace2 = go.Bar(
    x=cl1,
    y=cl2,
    name='Swarms',
)

layout = go.Layout(
    xaxis_title="Desert Locust Reports",
    #barmode='group'
)

data = [trace1, trace2]

fig = go.Figure(
    data = data,
    layout = layout,
)

fig.layout.update(
    xaxis_type='category'
)

offline.plot(fig, filename='index.html')
