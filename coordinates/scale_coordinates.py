# This file will scale output coordinates to the shape and size of the tree lights,
# then return a list of ~500 RGB colour values which will be the colors object
import numpy as np
import csv

n_ybands = 20
n_xbands = 20

coords = []
indexes = list()
ys = []
xs = []
# opening the CSV file
with open("sample_coords.csv", mode='r')as file:

    # reading the CSV file
    csvFile = csv.reader(file)
    

    # displaying the contents of the CSV file
    for index in csvFile:
        coords.append(index)
    coords = np.array(coords)

    xs = coords[:,1]
    ys = coords[:,2]
    zs = coords[:,3]
    indexes = coords[:,1]

    y_range = max(ys)
    x_range = max(xs)

    def iterator(n_ybands, y_range):
        for band in range(n_ybands):
            y_window_lower = int(y_range) / 20 * band
            y_window_upper = int(y_range) / 20 * band+1
            print(y_window_lower, y_window_upper)
        


iterator(n_ybands, y_range)

# print(indexes)

    # print(coords)

