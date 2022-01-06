## example test of csvread in csvreader.py file
## require test.csv

import sys
sys.path.append("../src")
from csvreader import * 

file_name = "test.csv"
d = csvread(file_name,1)
print(d)
print(d[0])
