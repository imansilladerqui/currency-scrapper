# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import pymysql
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
from maguiturposadas.items import MaguiturposadasItem

class MaguiturposadasPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('paisanoscreando.cskgygedfvbd.sa-east-1.rds.amazonaws.com', 'paisanoscreando', 'LaClaveSecreta', 
                                    'cambioposadas', charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):    
            self.cursor.execute("""INSERT INTO cambioposadas.casa_maguitur (entidad, compra, venta, dia, hora)  
                        VALUES (%s, %s, %s, %s, %s)""", 
                    (item['entidad'].encode('utf-8'),
                        item['compra'].encode('utf-8'),
                        item['venta'].encode('utf-8'),
                        item['dia'].encode('utf-8'),
                        item['hora'].encode('utf-8')))
            self.conn.commit()
            return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()