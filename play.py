#In this file I use as playing around with what I want to do!
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

print("\033c")
deaths = pd.read_csv('eu_terrorism_fatalities.csv', index_col='Year')
# print(deaths.head())

#Here I have a list which will hold all of the countries.
states = ["Belgium", "Denmark", "France", "Germany", "Greece", "Ireland", "Italy", "Luxembourg", "Netherlands", "Portugal", "Spain", "United Kingdom"]
#I then create more lists which will hold the number of deaths per year, the years and
basicCount = []
totalCount = []
years = []
total = 0

#Setting the starting year to 1970-where my data starts. 
year = 1970 


#This line takes a specific state in the list and sets it equal to specificCountry
specificCountry = deaths[['United Kingdom']]
yearData = specificCountry.loc[[year]]
deathsatYear = yearData.iat[0,0]
print(deathsatYear)