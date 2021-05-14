import pandas as pd;
import plotly.figure_factory as ff

df = pd.read_csv("Data.csv")
AvgRating = dict(df)["Avg Rating"]

graph = ff.create_distplot([AvgRating], ["Avg Rating"])
graph.show()