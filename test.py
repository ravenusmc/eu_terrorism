#In this file I use as playing around with what I want to do!
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

print("\033c")
deaths = pd.read_csv('eu_terrorism_fatalities.csv', index_col='Year')
# print(deaths.head())

states = ["Belgium", "Denmark", "France", "Germany", "Greece", "Ireland", "Italy", "Luxembourg", "Netherlands", "Portugal", "Spain", "United Kingdom"]
basicCount = []
totalCount = []
years = []
total = 0

year = 1970 
while year < 2015:
  for state in states:
    specificCountry = deaths[[state]]
    yearData = specificCountry.loc[[year]]
    deathsatYear = yearData.iat[0,0]
    basicCount.append(deathsatYear)
  years.append(year)
  year += 1 
value = 0
num1 = 0
num2 = 12
while value < 45:
  deathTotal = basicCount[num1:num2]
  summation = sum(deathTotal)
  totalCount.append(summation)
  num1 = num1 + 12
  num2 = num2 + 12 
  value += 1
print(totalCount)
print(years)
plt.plot(years, totalCount, linewidth=2, c="crimson")
plt.title("Death Toll By Year", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Deaths", fontsize=12)
plt.show()



  ###Attempt number 2
  # a = basicCount[0:12]
  # b = basicCount[13:24]
  # valueA = sum(a)
  # valueB = sum(b)
  # totalCount.append(valueA)
  # totalCount.append(valueB)
  # totalCount.append(valueC)
  # print(totalCount)


  ###WAY NUMBER 1
  # for value in basicCount:
  #   total = total + value
  # totalCount.append(total)
 






