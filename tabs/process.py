# @author Daniel Grooms
# @file process.py

# Test processing functions from the web crawler output

import sys
import xml.etree.ElementTree as xmltree
import parsefuncs

def main(file):
    tree = xmltree.parse(file)
    root = tree.getroot()
    value = root[0][0][0]
    rawTab = value.text

    if("\M" in rawTab):
        rawTab = parsefuncs.removeLineEndings(rawTab)

    cleanTab = parsefuncs.parseTab(rawTab)

    print("Clean tab is:")
    for line in cleanTab:
        print line

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please pass a file to parse')
    else:
        filename = sys.argv[1]

        main(filename)
