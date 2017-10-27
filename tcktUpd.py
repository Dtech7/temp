#CSci 127 Teaching Staff
#October 2017
#Count which cars got the most parking tickets

#Updated by: Neil Felix
#Date: 10/26/17
#Update Info: allows user to input file and search Attribute

#Import pandas for reading and analyzing CSV data:
import pandas as pd

fileNm = input('Enter file name: ')
attr = input('Enter serch attribute: ')

#csvFile = "tickets.csv"			#Name of the CSV file
tickets = pd.read_csv(fileNm)		#Read in the file to a dataframe
print("The 10 worst offenders are:")
print(tickets[attr].value_counts()[:10])





#print(tickets) 				#Print out the dataframe
