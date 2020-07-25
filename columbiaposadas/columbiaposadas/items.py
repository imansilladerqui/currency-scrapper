# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ColumbiaposadasItem(scrapy.Item):
    entidad = scrapy.Field()
    compra = scrapy.Field()
    venta = scrapy.Field()
    dia = scrapy.Field()
    hora = scrapy.Field()
    pass
