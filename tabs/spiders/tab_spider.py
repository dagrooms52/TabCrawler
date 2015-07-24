# @file tab_spider.py
# @author Daniel Grooms

# Initial implementation of a spider that will crawl ultimate-guitar.com
# and store tabs and chord sheets, to possibly display in better quality
# in the final application

import scrapy

from tabs.items import TabSheet

class TabReader(scrapy.Spider):
    name = "tab"
    allowed_domains = ["ultimate-guitar.com"]
    start_urls = []

    def __init__(self, link = ""):
        if(link == ""):
            print("Improper link format (tab_spider.py)")
            return
        else:
            print(link)
            self.start_urls.append(link)

    def parse(self, response):
        for page in response.xpath(".//div[@class='tb_ct']/div[@id='cont']"):
            sheet = TabSheet()
            sheet['tabs'] = page.xpath('pre[not(@*)]/text()').extract()
            yield sheet
