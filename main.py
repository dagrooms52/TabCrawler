# @author Daniel Grooms
# @file main.py

# The main command-line application for the Tab Crawler

import sys
import tabs

import xml.etree.ElementTree as xmltree
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import tabs.parsefuncs as parsefuncs
import tabs.spiders.tab_spider as Spiders

def main(tabLink):
    if(tabLink.find("ultimate-guitar.com")):
        tabSpider = Spiders.Ultimate(tabLink)
    elif(tabLink.find("guitartabs.cc")):
        tabSpider = Spiders.TabCC(tabLink)
    else:
        print("Domain name not supported.")
        return

    # Make a process to instantiate a Ultimate spider with the given
    # arguments and make it crawl the link
    process = CrawlerProcess(get_project_settings())
    process.crawl(tabSpider, link=tabLink)
    process.start()

    # Link has been scraped, now process it
    tree = xmltree.parse(tabs.pipelines.filename)
    root = tree.getroot()
    value = root[0][0][0]
    rawTab = value.text

    if("\M" in rawTab):
        rawTab = parsefuncs.removeLineEndings(rawTab)

    cleanTab = parsefuncs.parseTab(rawTab)

    print("Clean tab is:")
    count = 0
    for line in cleanTab:
        count += 1
        print line
        if(count % 6 == 0):
            print(" ")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Prompt for a tab link, or else view available tabs
        tabLink = "{}".format(raw_input("Enter a tab link: "))
    else:
        tabLink = "{}".format(sys.argv[1])

    main(tabLink)
