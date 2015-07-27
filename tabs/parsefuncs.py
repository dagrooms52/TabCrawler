# @file tabparser.py
# @author Daniel Grooms

# Parsing functions for guitar tabs

def parseTab(raw):
    tab = []

    # Split the tab into an array of its lines
    lines = raw.split("\n")

    for line in lines:
        if(line.count("-") > 5):
            tab.append(line)

    return tab

def removeLineEndings(raw):
    result = ''.join(raw, "\\M")
    return result
