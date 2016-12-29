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
lineCount = 0
#read in each line of raw csv or .txt product file
for line in fhand:
    #code for how to skip header row
    if firstline:
        firstline = False
        continue
    #lets just process the first 10 lines for now
    if lineCount <10:
        line = line.rstrip()
        #split the line into words at each comma
        words = line.split(",")
        #if row is blank, skip
        if len(words)==0:
            continue
        #for each field in the row from the input file), print out the string
        for word in words:
            print word,
    lineCount = lineCount + 1
    print 'the line we just finished processing is: ', lineCount
