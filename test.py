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
#I then start a while loop using the year variable that will end when year is equal to 2015
while year < 2015:
  #I then start a second loop to loop through the states list which I built above. 
  for state in states:
    #This line takes a specific state in the list and sets it equal to specificCountry
    specificCountry = deaths[[state]]
    #This line will get me the number of deaths at the specified year for the country that
    #specific country is currently set to. 
    yearData = specificCountry.loc[[year]]
    #I need the exact value that yearData gives me so I need to use iat which will return 
    #That exact value-which in this case is in integer.
    deathsatYear = yearData.iat[0,0]
    #I then append that value to the basicCount list.
    basicCount.append(deathsatYear)
  #I also need to append the current year that the loop is on to the years list.
  years.append(year)
  #I then add one to the year to increment the loop. 
  year += 1 

#At this point I have all of the values per country in a list called basicCount. However, those 
#values need to be summed per year and then pushed into another list entitled totalCount which 
#was declared above. I attempted to use another loop here but it was not working. (See attempt 
# number one below.) Thus, I switched over to using slices-something that I have not used much in 
#Python and they got the job done for me! 

#First I need a count variable which I called value. It is set to 0 to start. 
value = 0
#The num1 and num2 variables will be placed into the slice and will determine where the slice occurs. 
num1 = 0
num2 = 12

#Now this while loop will keep on going as long as value is less than 45. The reason it is set to 45
#is because I have 45 years of data. Furthermore, I have 12 points of data for each year which need to 
#be summed. Thus, I have to start at position 0 to 11, slice out that data, sum it, then append that 
#summation to the totalCount list. I then increase the num1 and num2 variables by 12 which will go 
#through the next increment. The value is increased by one as well. 
while value < 45:
  deathTotal = basicCount[num1:num2]
  summation = sum(deathTotal)
  totalCount.append(summation)
  num1 = num1 + 12
  num2 = num2 + 12 
  value += 1
print(totalCount)
print(years)

#All of this will plot the data. The years and totalCount lists are both used to create the line plot.
plt.plot(years, totalCount, linewidth=2, c="crimson")
plt.title("Death Toll By Year", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Deaths", fontsize=12)
plt.show()

### Attempt NUMBER 1
# for value in basicCount:
#   total = total + value
# totalCount.append(total)


### Attempt number 2
# a = basicCount[0:12]
# b = basicCount[13:24]
# valueA = sum(a)
# valueB = sum(b)
# totalCount.append(valueA)
# totalCount.append(valueB)
# totalCount.append(valueC)
# print(totalCount)



 






