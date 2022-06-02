## read the csv file using reader function

import csv
# from csv import reader

with open('file.csv', 'r') as f:
    read = csv.reader(f)
    # read = reader(f)
    # iterator 
    next(read)
    for i in read:
        print(i)