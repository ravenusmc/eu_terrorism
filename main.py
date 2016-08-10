#Main File for the project. 

def main():
  print("Welcome to European Terrorism Data.")
  print("This program will allow the user to see the amount of people killed by terrorism.")
  print("The data goes from 1970 to the present.")
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
  print("Welcome to the main menu")
  print("1. Look at data")
  print("2. Quit")


main()
