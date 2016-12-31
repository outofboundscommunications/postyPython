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
    fname = "GoogleMerchantCenterfeed-UpdateQuantitiesV2-LiveFeed10052016-short.csv"
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()
#read in entire file into a string variable
inp = fhand.read()
#print len(inp)
#print inp
#print inp.count("\n")

myDic = {}
skipWordList = ['id','title','description','link','condition','price','availability','image link','gtin','mpn','brand','google product category','shipping weight','sale price','sale price effective date','additional image link','product type','custom label 0']
words = inp.split(",")
for word in words:
    #skip header row
    if any(substring in word for substring in skipWordList):
        print 'skipped this word cause in list: ',word
        continue
    print '-', word
    #store key/value pairs in dictionary
    #key is product ID, value is a list of the rest of the columns for that product
    #mydict = {"message": {"hello": 123456}}

'''

#define variables
firstline = True
lineCount = 0
#read in each line of raw csv or .txt product file
#and replace line breaks with a space
for line in fhand:
    #skip header row
    if firstline:
        firstline = False
        continue
    print 'this is the line before i strip it: ',line
    line = line.replace("\r\n"," ")
    print 'this is the line after i strip it: ', line
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
'''
