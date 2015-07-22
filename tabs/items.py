# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# Item to get tabs from site
class TabSheet(scrapy.Item):
    tabs = scrapy.Field()
    pass

# Chords are also on the site
class ChordSheet(scrapy.Item):
    chords = scrapy.Field()
    pass
