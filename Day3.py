# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:20:25 2019

@author: STEM
"""
#listing the type of chocolate along with the amount in the box
Cadbury1 = "Dark Chocolate"
Cadbury2 = "Milk Chocolte"
Cadbury3 = "White Chocolate"
DarkChocolate = 5
WhiteChocolate = 8
MilkChocolate = 6
print("This box of chocolate contains", DarkChocolate,"pieces of", Cadbury1 ,
      ",", WhiteChocolate,"pieces of", Cadbury3, ", and", MilkChocolate,"pieces of", 
      Cadbury2)

#simplifying how to do the same program called dicts
cadbury1 = {"Dark Chocolate":5}
cadbury2 = {"Milk Chocolate": 6}
cadbury3 = {"White Chocolate": 8}

#another simpler dict to make it into one line
chocolates = {"dark":5, "whites":8, "milk":3}
print(chocolates)

#example of dicts that include name, gender, and age
students = {"Steve":32, "Lia":28, "Vin":45, "Katie":38}
print(students)

#example of a list
studentList = [["Steve",32,'M'],["Lia",28,'F'],["Vin",45,'M'], ["Katie",38,'F']]
print(studentList)

#how to print two dicts
combination = [chocolates,students]
combination

#the panda library
import pandas
dir(pandas)
studentdf = pandas.DataFrame(studentList,columns=("Name", "Age", "Gender"))
studentdf

#create a data frame to represent the information of the chocolate box
allChocolates = [["Milk",3],["White",8],["Dark",5]]
chocolateBox = pandas.DataFrame(allChocolates, columns=("Type","Amount"))
chocolateBox

#reference columns from data frames
studentdf["Name"]
studentdf["Gender"]
chocolateBox["Amount"]

#create a data frame of student info (refresher)
studentList2 = [["Steve",23,'M'], ["Ashlyn",16,'F'], ["John",45,'M'], ["Sally",18,'F']]
studentList2
import pandas
studentdf = pandas.DataFrame(studentList2,columns=("Name","Age","Gender"))
studentdf
studentdf = pandas.DataFrame(studentList2,columns=("Name","Age","Gender"), 
                             index=("1","2","3","4"))
studentdf

#using the plotly library for the student information
import plotly
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go
studentbar = go.Bar(x=studentdf["Name"], y=studentdf["Age"])
plot([studentbar])

#using the plotly library for the box of chocolates
import plotly
from plotly.offline import plot
import plotly.graph_objs as chocobox
ChocoBoxBar = chocobox.Bar(x=chocolateBox["Type"],y=chocolateBox["Amount"])
plot([ChocoBoxBar])
titles = chocobox.Layout(title = "Number of Chocolates By Type")
ChocoBoxBar = chocobox.Bar(x=chocolateBox["Type"],y=chocolateBox["Amount"])
fig = chocobox.Figure(data=[ChocoBoxBar], layout=titles)
plot(fig)













