#In this file I use as playing around with what I want to do!
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

print("\033c")
deaths = pd.read_csv('eu_terrorism_fatalities.csv', index_col='Year')

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

count  = []
years = []
state = input("Please enter a country to examine: ")
specificCountry = deaths[[state]]
year = 1970
while year < 2015:
  yearData = specificCountry.loc[[year]]
  deathsAtYear = yearData.iat[0,0]
  count.append(deathsAtYear)
  years.append(year)
  year += 1

plt.plot(years, count, linewidth=2, c="blue")
plt.title("Death Toll By Year", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Deaths", fontsize=12)
plt.show()







# print(play.iat[0,0])
# print(test.loc[[1986]])

# print(deaths.loc[[1973,1974]])

