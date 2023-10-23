# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BookItem(scrapy.Item):

    title = scrapy.Field()
    upc = scrapy.Field()
    price = scrapy.Field()
    product_type = scrapy.Field()
    tax = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
