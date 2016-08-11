#In this file I use as playing around with what I want to do!
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

print("\033c")
#colNames = ['Year', 'Belgium', 'Denmark', 'France', 'Germany', 'Greece', 'Ireland', 'Italy', 'Luxembourg', 'Netherlands', 'Portugal', 'Spain', 'United Kingdom']
#deaths = pd.read_csv('eu_terrorism_fatalities.csv')
deaths = pd.read_csv('eu_terrorism_fatalities.csv', index_col='Year')
print("Welcome to single country deaths")
print("Belgium")
print("Denmark")
print("France")
print("Germany")
print("Greece")
print("Ireland")
print("Italy")
print("Luxembourg")
print("Netherlands")
print("Portugal")
print("Spain")
print("United Kingdom")
# print(deaths.head())
#choice = input("What country do you want to look at: ")
# test = deaths[[choice.title()]]
# year = input("Please give me a starting year: ")
#print(deaths[choice.title()])
#print(test.dtypes)

count  = []
test = deaths[['France']]
print(test)
num = test.France.count()
print(num) #I need to get specific year 



### Specific Year version:
# count = []
# year = input("please enter in a year: ")
# shape = input("Please enter in a shape: ")
# df = ufo[ufo.Time.str.contains(year)]
# specificShape = df[df.Shape == shape.upper()]
# number = specificShape.Shape.count()
# count.append(int(number))
# print(count)

