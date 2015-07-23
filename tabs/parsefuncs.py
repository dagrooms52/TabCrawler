# @file tabparser.py
# @author Daniel Grooms

# Parsing functions for guitar tabs

import re

TAB_RGX = r'^[A-Za-z\#]{0,2}[\-\|\\\/\~0-9]+\s*[xX0-9]*$'

def parseTab(raw):
    tab = []

    # Split the tab into an array of its lines
    lines = re.split("\n+", raw)

    for line in lines:
        match = re.search(TAB_RGX, line)
        if match:
            tab.append(match.group())

    return tab

def removeLineEndings(raw):
    result = ''.join(raw, "\\M")
    return result
