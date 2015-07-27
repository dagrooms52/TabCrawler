# @file tab_spider.py
# @author Daniel Grooms

# Initial implementation of a spider that will crawl ultimate-guitar.com
# and store tabs and chord sheets, to possibly display in better quality
# in the final application

import scrapy

from tabs.items import TabSheet

class Ultimate(scrapy.Spider):
    name = "ultimate"
    allowed_domains = ["ultimate-guitar.com"]
    start_urls = []

    def __init__(self, link=""):
        if(link == ""):
            print("Improper link format (ultimate)")
        else:
            print(link)
            self.start_urls.append(link)

    def parse(self, response):
        for page in response.xpath(".//div[@class='tb_ct']/div[@id='cont']"):
            sheet = TabSheet()
            sheet['tabs'] = page.xpath('pre[not(@*)]/text()').extract()
            yield sheet

class TabCC(scrapy.Spider):
    name = "tabcc"
    allowed_domains = ["guitartabs.cc"]
    start_urls = []

    def __init__(self, link=""):
        if(link == ""):
            print("Improper link format(tabcc)")
        else:
            print(link)
            self.start_urls.append(link)

    def parse(self, response):
        for page in response.xpath(""".//div[@class='maincont']/
                                        div[@class='tabcont']"""):
            sheet = TabSheet()
            sheet['tabs'] = page.xpath('pre/text()').extract()
            yield sheet
