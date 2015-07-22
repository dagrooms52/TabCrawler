# -*- coding: utf-8 -*-

# @file items.py
# @author Daniel Grooms

import scrapy

# Item to get tabs from site
class TabSheet(scrapy.Item):
    tabs = scrapy.Field()
    pass

# Chords are also on the site
class ChordSheet(scrapy.Item):
    chords = scrapy.Field()
    pass
