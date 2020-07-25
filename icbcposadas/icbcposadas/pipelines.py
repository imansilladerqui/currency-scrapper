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
from icbcposadas.items import IcbcposadasItem
import constants

class IcbcposadasPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(constants.database_env, constants.table, constants.password, 
        constants.user, charset="utf8",
        use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):    
            self.cursor.execute("""INSERT INTO %s.banco_icbc (entidad, compra, venta, dia, hora)  
                        VALUES (%s, %s, %s, %s, %s)""", 
                    (constants.table,
                        item['entidad'].encode('utf-8'),
                        item['compra'].encode('utf-8'),
                        item['venta'].encode('utf-8'),
                        item['dia'].encode('utf-8'),
                        item['hora'].encode('utf-8')))
            self.conn.commit()
            return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()