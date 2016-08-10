#Main File for the project.
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

from valid import *
 
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
  print("Welcome to the data section")
  print("Here you will decide how you want to look at the data")
  deaths = pd.read_csv('eu_terrorism_fatalities.csv')
  print("1. Individual Country")
  print("2. Multiple Countries")
  print("3. Main Menu")
  print("4. Quit")
  choice = int(input("What is your choice? "))
  while not validData(choice):
    choice = int(input("What is your choice? "))
  if choice == 1:
    singleCountry(deaths)
  elif choice == 2:
    multipleCountry(deaths)
  elif choice == 3:
    mainMenu()
  elif choice ==  4:
    print("Thank you for stopping by!")
    print("I hope that you come again!")

def singleCounty(deaths):
  print("\033c")
  print("Welcome to single country deaths")
  print("Belgium")
  print("Denmark")
  print("3. France")
  print("4. Germany")
  print("5. Greece")
  print("6. Ireland")
  print("7. Italy")
  print("8. Luxembourg")
  print("9. Netherlands")
  print("10. Portugal")
  print("11. Spain")
  print("12. United Kingdom")
  choice = input 



main()


























