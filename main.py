#Main File for the project.
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

from valid import *

#To do: 1. Make a graph for multiple countries 2. Make a function that will have data for all states and 
#then total by year. 
 
def main():
  print("\033c")
  print("Welcome to European Terrorism Data.")
  print("This program will allow the user to see the amount of people killed by terrorism.")
  print("The data has data from 1970 to the present.")
  print("1. Use the program")
  print("2. Quit")
  choice = int(input("What is your choice?(1/2) "))
  while not validMain(choice):
    choice = int(input("What is your choice?(1/2) "))
  if choice == 1:
    mainMenu()
  elif choice == 2:
    print("Thank you for stopping by!")
    print("I hope that you come again!")

def mainMenu():
  print("\033c")
  print("Welcome to the main menu")
  print("1. Look at data")
  print("2. Quit")
  choice = int(input("What is your choice? "))
  while not validMain(choice):
    choice = int(input("What is your choice? "))
  if choice == 1:
    data()
  elif choice == 2:
    print("Thank you for stopping by!")
    print("I hope that you come again!")

def data():
  print("\033c")
  print("Welcome to the Data Section")
  print("Here you will decide how you want to look at the data")
  deaths = pd.read_csv('eu_terrorism_fatalities.csv', index_col='Year')
  print("1. Individual Country")
  print("2. Multiple Countries")
  print("3. Total Deaths")
  print("4. Main Menu")
  print("5. Quit")
  choice = int(input("What is your choice? "))
  while not validData(choice):
    choice = int(input("What is your choice? "))
  if choice == 1:
    singleCountry(deaths)
  elif choice == 2:
    multipleCountry(deaths)
  elif choice == 3:
    totalDeaths(deaths)
  elif choice ==  4:
    mainMenu()
  elif choice == 5:
    print("Thank you for stopping by!")
    print("I hope that you come again!")

def singleCountry(deaths):
  print("\033c")
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
  state = input("What state do you want to look at: ")
  count  = []
  years = []
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

def multipleCountry(deaths):
  print("\033c")
  print("Welcome to Multiple Country Deaths")
  print("Here enter the countries that you want to examine")
  print("Leave a blank space when you are done entering in countries.")
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
    while not validMultiple(state):
      print("You did not enter a country correctly!")
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

def totalDeaths(deaths):
  print("\033c")

main()


























