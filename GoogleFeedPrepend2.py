__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.

'''
read thru simple csv file that just contains one column (product title)
for each line, if there is already a string containing '50', then skip
if there is the string 'calendar', skip
otherwise:
    replace the hyphen with: - Set of 50 -

example:
Balloon Party Postcard - Business Birthday PostCards would be changed to:
Balloon Party Postcard - Set of 50 - Business Birthday PostCards

'''

import string
import csv

fname = raw_input('Enter the file name: ')
if len(fname)==0:
    fname = "PostyoneColumn.csv"
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

#define list of product titles we revised
productTitles = []

rowCounter = 0
firstline = True
#read in each line of csv feed file
for line in fhand:
    if firstline: #skip first line
        firstline = False
        continue
    line = line.rstrip()
    #increment the rowCounter by 1
    rowCounter = rowCounter +1
    print 'processing row: ', rowCounter, ' in the csv file.'
    print 'the value is: ', line
    #if no dash in line, skip, its a calendar
    if "-" not in line:
        productTitles.append(line)
        continue
    #if we already added the '50' text, don't need to do again so skip this line
    if '50' in line:
        productTitles.append(line)
        continue
    #split the column into strings at the '-'
    words = line.split("-")
    #if length of words is not 2, we don't want it
    '''
    if len(words) !=2
        productTitles.append(line)
        continue
    '''
    #now we have string fragment (words[1]) we want to operate on (the one after the dash)
    words[1] = "- Set of 50 - " + words[1]
    newTitle = words[0] + words[1]
    productTitles.append(newTitle)

print 'the number of rows processed is: ',rowCounter
for product in productTitles:
    print 'the new title is: ', product

#write the new titles to another csv
'''
outfile = open('text.csv',"w")
for product in productTitles:
    writer = csv.writer(outfile,delimiter=',')
    writer.writerows(product)
outfile.close()

'''
fout = open('postyproducts.csv','w')

#str1 = "".join(categories)
#str1 = "".join(str(x) for x in categories)
#str1 = ',\n'.join(str(v) for v in productTitles)
str1 = '\n'.join(str(v) for v in productTitles)
fout.write(str1)
fout.close()
