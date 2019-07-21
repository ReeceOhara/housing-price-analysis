import csv
import re
import numpy
from matplotlib import pyplot as plt

patt = re.compile('\d{4}')
y = []
y2 = []
x = []

##Getting the house sale prices and the year of the sale
with open('./house-sales/kc_house_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = 0
    for row in csv_reader:
        #Limiting the data read, can remove if you want to read all 21K lines of the .csv
        if count == 100:
            break
        year = patt.search(row[1])
        if not year:
            year = '0'
        else:
            year = year.group()
        #Making sure the data was okay
        # print(row[2])
        # print(year)
        y.append(row[2])
        x.append(year)
        count += 1

with open('./interest-rates/index.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = 0
    for row in csv_file:
        if count == 100:
            break
        if not row[6].isdigit():
            y2.append('0')
        else:
            y2.append(row[6])
#Sorting the arrays and then plotting them
x = numpy.sort(x)
y = numpy.sort(y)
y2 = numpy.sort(y2)
plt.plot(y2)
plt.show()