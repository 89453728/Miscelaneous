## example test of csvread in csvreader.py file
## require test.csv

import sys
sys.path.append("../src")
from csvreader import * 

def printAll(al,index):
        for idx,elem in enumerate(al):
                print("--------------------------")
                print("Element " + str(idx))
                for a in index:
                        print(a + ": " + elem[a])
                print("--------------------------")

file_name = "test.csv"
print("printing all the file")
d = csvread(file_name)
print("")
print("raw print:")
printAll(d,["nombre","edad"])
print("printing 2 elements")
d = csvread(file_name,2)
print("")
print("raw print")
printAll(d,["nombre","edad"])
