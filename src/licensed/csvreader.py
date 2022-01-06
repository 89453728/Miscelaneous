## csvreader.py
## Copyright (C) 2022-2023  Yassin Achengli <0619883460@uma.es>
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
## csv format files reader and convert in object array
##
## INDEX
## error:       takes string as argument and print it in the screen 
##              as a error message
## insert:      takes three arguments, the list where we want to append
##              ,the list of indexes and the list of elements to append 
##              into the list. It returns the new list if length of 
##              element and length of index match and False in otherwise
## csvread:     takes two parameters, the second is optional, file_name 
##              is the file to converse and lines are the lines to read
##              but if you let it blank, it will be set as -1 and csvread
##              is going to read all the file.
##
## @example
## ## Using the file test.csv
## 
## from csvreader import csvread
## file_name = "test.csv"
## data = csvread(file_name)
## print(data)
##      => [{'nombre': 'yassin', 'edad': '22'}, {'nombre': 'nadia', 'edad': '19'}, 
##      {'nombre': 'karim', 'edad': '29'}, {'nombre': 'mama', 'edad': '56'}, 
##      {'nombre': 'papa', 'edad': '62'}]
## data = csvread(file_name,2)
## print(data)
##      => [{'nombre': 'yassin', 'edad': '22'}]
## @end example
##
def error(msg):
        print("Error >> " + msg)

def insert(All, element, index):
        if (len(element) != len(index)):
                error("element and index must be the same size <insert error>")
                return False
        prob = {}
        for a in range(0,len(index)):
                prob[index[a]] = element[a]
        All.append(prob)
        return All

def csvread (file_name, lines = -1):
        if (lines == 0):
                return False
        All = []
        try:
                f = open(file_name,'r')
        except IOError:
                error("couldn't open the file " + file_name)
        index_words = f.readline()
        if (len(index_words) < 2):
               error("csv file is empty")
               return False
        index_words = index_words.replace(' ','')
        index_words = index_words.replace('\n','')
        index_words = index_words.lower()
        index_list = index_words.split(',')
        for idx, val in enumerate(index_list):
                for a in range(0,idx):
                        if(index_list[idx]==index_list[a]):
                                error("error, two indexes are the same")
                                return False
         
        line = 0
        buff = f.readline()
        if (lines == -1):
                while (buff != ""):                    
                        buff = buff.replace(' ','')
                        buff = buff.replace('\n','')
                        elements = buff.split(',')               
                        temp = insert(All,elements,index_list)
                        if (temp != False):
                                All = temp
                        buff = f.readline()
        else:
                while(buff != "" and line < lines):
                        line+=1 
                        buff = buff.replace(' ','')
                        buff = buff.replace('\n','')
                        elements = buff.split(',')
                        temp = insert(All,elements,index_list)  
                        if(temp != False):
                                All = temp
                        buff = f.readline()
        f.close()
        return All
