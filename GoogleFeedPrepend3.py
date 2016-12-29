__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.
#__author__ = 'outofboundscommunications'
#To change this template use Tools | Templates.

'''
read thru simple csv file that just contains two columns (id and product title)
for each line, if there is already a string containing '50', then skip
if there is the string 'calendar', skip
otherwise:
    replace the hyphen with: - Set of 50 -

example:
Balloon Party Postcard - Business Birthday PostCards
would be changed to:
Balloon Party Postcard - Set of 50 - Business Birthday PostCards

'''

import string
import csv

fname = raw_input('Enter the file name: ')
if len(fname)==0:
    fname = "PostyoneColumn2.csv"
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

#define list of product titles we revised
productTitles = []
#define dictionary
prodDic = dict()
#set rowCounter to zero
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
    #print 'processing row: ', rowCounter, ' in the csv file...'
    #print 'the record is: ', line
    #split line into two fragments
    words = line.split(",")
    #print 'the words split up are: ', words
    #note: words[0] = sku/id, words[1] = productTitle
    #example of data split for assortment:
        #original data: AO501,Birthday Assortment - Birthday Card Assortment Packs
        #after split on comma: [AO501,Birthday Assortment - Birthday Card Assortment Packs]
    #example of data split for calendar:
        #original data: D6110U-4A,American Flag Logo Calendar Cards
        #after split on comma: [D6110U-4A,American Flag Logo Calendar Cards]

    #if length of words is zero, that means the row is empty, its blank, so skip
    if len(words)==0:
        continue
    '''
    #if the product title contains 'calendar', skip
    if "calendar" in words[1].lower():
        continue
    '''
    #if product title contains calendar then append 'Set of 50'
    if "calendar" in words[1].lower():
        mynewProdName = words[1] + " (Set of 50)"
        #and add to dictionary
        prodDic[words[0]] = mynewProdName
        continue
    #if product title contains assortment, then we need to split again on the '-' and modify with 'Pack of 50 Assorted Cards' to end
    if "assortment" in words[1].lower():
        #split the second column (prod name) into substrings at the '-'
        prodnamefrags = words[1].split("-")
        #build the new product name by replacing fragement after hyphen with "Pack of 50 Assorted Cards"
        mynewProdName = prodnamefrags[0] + " - Pack of 50 Assorted Cards"
        #add the product to the dictionary
        prodDic[words[0]] = mynewProdName
        continue
    #split the second column (prod name) into substrings at the '-'
    prodnamefrags = words[1].split("-")
    #now we have string fragment (prodnamefrags[1]) we want to operate on (the one after the dash)
    #prepend the string 'Set of 50'
    prodnamefrags[1] = "- Set of 50 - " + prodnamefrags[1]
    #build the new product name
    mynewProdName = prodnamefrags[0] + prodnamefrags[1]
    #add the product to the dictionary
    prodDic[words[0]] = mynewProdName
    #print 'added key: ', words[0], ' and value: ', mynewProdName, ' to dictionary.'

print 'the number of rows processed is: ',rowCounter
for key in sorted(prodDic):
    print key, prodDic[key]

#write the new titles to another csv
fout = open('postyproducts.csv','w')

'''
#str1 = ',\n'.join(str(v) for v in productTitles)
str1 = '\n'.join(str(v) for v in productTitles)
fout.write(str1)
fout.close()

'''
for key in sorted(prodDic.keys()):
    fout.write(str(key) + "," + str(prodDic[key]) + "\n");
