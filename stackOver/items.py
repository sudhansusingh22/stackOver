# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class StackItem(Item):
    # Title of question
    title = Field()
    # Url of question
    url = Field()
    # Usename, who has posted it
    userName = Field()
    #User url
    userUrl = Field()

    pass
