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
    fname = "GoogleMerchantCenterfeed.csv"
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

#define list
products = []

rowCounter = 0
#read in each line of csv file
for line in fhand:
    line = line.rstrip()
    #split the line into words at each comma
    words = line.split(",")
    #reset word counter
    counter = 0
    #if length of row is zero, its blank, so skip
    if len(words)==0:
        continue
    #for each field in the row, print out the string
    for word in words:
        print word
        counter = counter +1
    #increment the rowCounter by 1
    rowCounter = rowCounter +1
    print 'the number of values/words in this line is: ', counter
