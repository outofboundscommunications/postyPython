__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.

'''
read thru adwords feed line by line and prepend the
appropriate string

case 1:
if product name contains 'assortment':
    split the row at the hyphen
    for the string fragment after the hyphen:
        insert "- Pack of 50 Assorted Cards - "
else:
    split the row at the hyphen
'''

'''
example data:

Birthday Assortment - Birthday Card Assortment Packs

Green Leaves Birthday Postcard - Birthday PostCards

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

#define list of products, its gonna be a list of lists
products = []

rowCounter = 0
firstline = True
assortCount = 0
otherCount = 0
#read in each line of csv feed file
for line in fhand:
    if firstline: #skip first line
        firstline = False
        continue
    line = line.rstrip()
    #split the line into words at each comma
    words = line.split(",")
    print words
    #if length of words is zero, that means the row is empty, its blank, so skip
    if len(words)==0:
        continue
    #if length of words is one, its a line with the envelope text so skip for now
    if len(words)==1:
        continue
    #locate the title field in the line (its the second value in list)
    #if an assortment, then replace the: 'Pack of 50 Assorted Cards'
    if words[1].find('Assort') > 0:
        #words[1] = "- Pack of 50 Assorted Cards"
        print 'i found an assortment'
        assortCount = assortCount+1
        products.append(words)
    else:
        #words[1] = "- Set of 50 - " + words[1]
        print 'i found something else'
        otherCount = otherCount +1
        products.append(words)

    #increment the rowCounter by 1
    rowCounter = rowCounter +1
    print 'processed row number: ', rowCounter

print 'the number of rows processed is: ',rowCounter
print 'the number of assortment products is: ', assortCount
print 'the number of other products is: ', otherCount
for product in products:
    print 'the id is: ', product[0], ' and its title is: ', product[1]
