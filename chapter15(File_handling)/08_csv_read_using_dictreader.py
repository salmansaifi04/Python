## dict_reader
from csv import DictReader
## it is a ordered dictionary

with open('file.csv', 'r') as f:
    read = DictReader(f)
    for i in read:
        # print(i)
        print(i['name'])



with open('file2.csv', 'r') as f:
    read = DictReader(f, delimiter = '|')
    for i in read:
        print(i)
        # print(i['name'])