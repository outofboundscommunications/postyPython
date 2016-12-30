__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.

'''
read through the bing feed line by line, each field is separated by comma
print out each line one by one

'''

import string

fname = raw_input('Enter the file name: ')
if len(fname)==0:
    fname = "GoogleMerchantCenterfeedUpdatedPrices.csv"
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

#define list
products = []
firstline = True
#read in first 10 lines only
for line in fhand:
    if firstline:
        firstline = False
        continue
    print line
    line = line.rstrip()
    #split the line into words at each comma
    words = line.split(",")
    #if row is blank, skip
    if len(words)==0:
        continue
    #for each field in the row from the input file), print out the string
    columnCount = 0
    for word in words:
        columnCount = columnCount +1
    print 'the number of columns in this row is: ', columnCount
