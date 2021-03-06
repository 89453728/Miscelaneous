## example test of csvread in csvreader.py file
## require test.csv

import sys
sys.path.append("../src")
from csvreader import * 

def printAll(al, index):
        for idx,elem in enumerate(al):
                
                print("------------------------")
                print("item " + str(idx))
                for a in index:
                        print(a + ": " + elem[a])
                print("------------------------")

file_name = "test.csv"
d = csvread(file_name)
print("\n\nAll " + file_name + " items: \n")
printAll(d,["nombre","edad"])
d = csvread(file_name,2)
print("\n\nTwo first items in " + file_name + ": \n")
printAll(d,["nombre","edad"])
