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
    start_urls = ["http://tabs.ultimate-guitar.com/o/onerepublic/apologize_tab.htm"]

    def parse(self, response):
        for page in response.xpath("//div[@class='tb_ct']/div[@id='cont']"):
            sheet = TabSheet()
            sheet['tabs'] = page.xpath('pre[not(@*)]/text()').extract()
            yield sheet
