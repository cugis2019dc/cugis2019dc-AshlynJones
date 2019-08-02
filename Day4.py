# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:26:21 2019

@author: STEM
"""

#importing all the libraries for the womens occupation data frame
import pandas as pd
import plotly
from plotly.offline import plot
import plotly.graph_objs as go

#reading the excel file into the data frame
wodf = pd.read_excel("GISdata.xlsx",sheet_name = "womenOccupation")
wodf

#use the bar graph function to graph all the data
woBar = go.Bar(x= wodf["occupation"], y= wodf["women"],
               marker = {"color": wodf["women"], "colorscale" : "Rainbow"})
titles = go.Layout(title = "Percentage of Women Employed by Occupation",
                   xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Occupation",
                        )
                   ),

                    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage",
                            )
                        )
                    )
fig = go.Figure(data=[woBar],layout = titles)
plot(fig)

#cancer cases
cc = pd.read_excel("GISdata.xlsx",sheet_name = "cancercases")
