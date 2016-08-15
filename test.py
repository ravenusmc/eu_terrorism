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

states = []

while True:
  state = input("Please enter a country to examine: ")
  if state == "":
    break
  else: 
    states.append(state)

belCount, denCount, franCount, gerCount, greCount, ireCount, itaCount, luxCount, netCount, porCount, spaCount, ukCount  = [], [], [], [], [], [], [], [], [], [], [], []
belYears, denYears, fraYears, gerYears, greYears, ireYears, itYears, luxYears, nethYears, portYears, spaYears, ukYears  = [], [], [], [], [], [], [], [], [], [], [], []

for state in states:
  specificCountry = deaths[[state]]
  year = 1970
  while year < 2015:
    if state == "Belgium":
      yearData = specificCountry.loc[[year]]
      deathsAtYear = yearData.iat[0,0]
      belCount.append(deathsAtYear)
      belYears.append(year)
      year += 1
    elif state == "Denmark":
      yearData = specificCountry.loc[[year]]
      deathsAtYear = yearData.iat[0,0]
      denCount.append(deathsAtYear)
      denYears.append(year)
      year += 1
    elif state == "France":
      yearData = specificCountry.loc[[year]]
      deathsAtYear = yearData.iat[0,0]
      franCount.append(deathsAtYear)
      fraYears.append(year)
      year += 1
    elif state == "Germany":
      yearData = specificCountry.loc[[year]]
      deathsAtYear = yearData.iat[0,0]
      gerCount.append(deathsAtYear)
      gerYears.append(year)
      year += 1
    elif state == "Greece":
      yearData = specificCountry.loc[[year]]
      deathsAtYear = yearData.iat[0,0]
      greCount.append(deathsAtYear)
      greYears.append(year)
      year += 1
    elif state == "Ireland":
      yearData = specificCountry.loc[[year]]
      deathsAtYear = yearData.iat[0,0]
      ireCount.append(deathsAtYear)
      ireYears.append(year)
      year += 1
    elif state == "Italy":
      yearData = specificCountry.loc[[year]]
      deathsAtYear = yearData.iat[0,0]
      itaCount.append(deathsAtYear)
      itYears.append(year)
      year += 1
    elif state == "Luxembourg":
      yearData = specificCountry.loc[[year]]
      deathsAtYear = yearData.iat[0,0]
      luxCount.append(deathsAtYear)
      luxYears.append(year)
      year += 1
    elif state == "Netherlands":
      yearData = specificCountry.loc[[year]]
      deathsAtYear = yearData.iat[0,0]
      netCount.append(deathsAtYear)
      nethYears.append(year)
      year += 1
    elif state == "Portugal":
      yearData = specificCountry.loc[[year]]
      deathsAtYear = yearData.iat[0,0]
      porCount.append(deathsAtYear)
      portYears.append(year)
      year += 1
    elif state == "Spain":
      yearData = specificCountry.loc[[year]]
      deathsAtYear = yearData.iat[0,0]
      spaCount.append(deathsAtYear)
      spaYears.append(year)
      year += 1
    elif state == "United Kingdom":
      yearData = specificCountry.loc[[year]]
      deathsAtYear = yearData.iat[0,0]
      ukCount.append(deathsAtYear)
      ukYears.append(year)
      year += 1

plt.plot(belYears, belCount, linewidth=2, c="black")
plt.plot(denYears, denCount, linewidth=2, c="yellow")
plt.plot(fraYears, franCount, linewidth=2, c="red")
plt.plot(gerYears, gerCount, linewidth=2, c="orange")
plt.plot(greYears, greCount, linewidth=2, c="crimson")
plt.plot(ireYears, ireCount, linewidth=2, c="firebrick")
plt.plot(itYears, itaCount, linewidth=2, c="blue")
plt.plot(luxYears, luxCount, linewidth=2, c="brown")
plt.plot(nethYears, netCount, linewidth=2, c="mediumblue")
plt.plot(portYears, porCount, linewidth=2, c="darkviolet")
plt.plot(spaYears, spaCount, linewidth=2, c="plum")
plt.plot(ukYears, ukCount, linewidth=2, c="orchid")
plt.title("Death Toll By Year", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Deaths", fontsize=12)
plt.show()



