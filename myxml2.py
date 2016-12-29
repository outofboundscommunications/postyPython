
#! usr/bin/python
# -*- coding: utf-8 -*-
import csv, sys, os
from lxml import etree

def main():
    csvFile = 'test.csv'
    xmlFile = open('myData.xml', 'w')
    csvData = csv.reader(open(csvFile), delimiter='\t')

    header = csvData.next()
    counter = 0
    root = etree.Element('root')

    for row in csvData:
        prod = etree.SubElement(root,'prod')
        for index in range(0, len(header)):
            child = etree.SubElement(prod, header[index])
            child.text = row[index].decode('utf-8')
            prod.append(child)

    result = etree.tostring(root, pretty_print=True)
    xmlFile.write(result)

if __name__ == '__main__':
    main()
