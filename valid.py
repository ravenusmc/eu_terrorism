#All of my valid functions will go here.

def validMain(choice):
  if choice == 1 or choice == 2:
    return True 
  else:
    return False 

def validData(choice):
  if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
    return True
  else:
    return False

def validMultiple(state):
  if state == "Belgium" or state == "France" or state == "Germany" or state == "Greece" or state == "Ireland" or state == "Italy" or state == "Luxembourg" or state == "Netherlands" or state == "Portugal" or state == "Spain" or state == "United Kingdom" or state == "":
    return True
  else: 
    return False




