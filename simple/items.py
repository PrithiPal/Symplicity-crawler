# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SimpleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JobItem(scrapy.Item) :

    job_description = scrapy.Field()
    job_id = scrapy.Field()
    job_identifier = scrapy.Field()

    job_title = scrapy.Field()

    pass
