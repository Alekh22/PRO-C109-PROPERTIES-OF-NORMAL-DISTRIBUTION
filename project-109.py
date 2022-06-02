from base64 import standard_b64decode
import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()
mean = statistics.mean(data)
standard_deviations= statistics.stdev(data)
mode = statistics.mode(data)
median = statistics.median(data)
print(mean)
print(standard_deviations)
print(mode)
print(median)