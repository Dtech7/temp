#Name: Neil Felix
#Date: 10/25
#Info: ask user for file name and output name; creates graph using data for file;
#       saves graph as the output name given.

import pandas as pd
import matplotlib.pyplot as plt

dtIn = input("Enter file name: ")
dtOut = input("Enter Output file name: ")
data = pd.read_csv(dtIn, skiprows=5)
data['Fraction Children'] = data['Total Children in Shelter']/data['Total Individuals in Shelter']

data.plot(x = "Date of Census", y = "Fraction Children")
#plt.show()

fig = plt.gcf()
fig.savefig(dtOut)

