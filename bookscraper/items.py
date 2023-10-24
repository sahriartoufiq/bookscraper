# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def serialize_num(value):

    pattern = r'[-+]?\d*\.\d+|\d+'
    matches = re.findall(pattern, value)

    return float(matches[0]) if matches else 0


class BookItem(scrapy.Item):

    title = scrapy.Field()
    upc = scrapy.Field()
    price = scrapy.Field(serializer=serialize_num)
    product_type = scrapy.Field()
    tax = scrapy.Field(serializer=serialize_num)
    description = scrapy.Field()
    url = scrapy.Field()
