from asyncio.windows_events import NULL
import plotly.express as px
import pandas as pd

#Simulation variables
arrival = 0.5
service = 1
queue_delay = 0
Ti = queue_delay + service
theta = 0
#W = T1 + T2 + . . . + Tp 
p = 10

test = 1

df = pd.DataFrame(dict(
    x = [test, 2, 3, 4],
    y = [1, 2, 3, 4]
))
graph = px.line(df, x="x", y="y", title="Simulation") 
graph.show()