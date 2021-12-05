# This file will scale output coordinates to the shape and size of the tree lights,
# then return a list of ~500 RGB colour values which will be the colors object

import csv

# opening the CSV file
with open("sample_coords.csv", mode='r')as file:

    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)
