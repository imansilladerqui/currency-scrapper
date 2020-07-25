import scrapy
import time
from scrapy.spiders import CrawlSpider
from maguiturposadas.items import MaguiturposadasItem

class MaguiturSpider(scrapy.Spider):
    name = 'maguiturposadas'
    allowed_domains = ['maguitur.net']
    start_urls = ['http://maguitur.net/prices.php']

    def parse(self, response):

        datadia = time.strftime("%d/%m/%Y")
        datahora = time.strftime("%H:%M:%S", time.localtime())
        compraDesdeLaWeb = response.xpath('/html/body/div/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[1]/text()').extract_first()
        compraNormalizado = compraDesdeLaWeb.replace(u'$ ', u'')[:-2]
        ventaDesdeLaWeb = response.xpath('/html/body/div/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[2]/text()').extract_first()
        ventaNormalizado = ventaDesdeLaWeb.replace(u'$ ', u'')[:-2]

        item = MaguiturposadasItem()
        item['entidad'] = 'Maguitur'
        item['compra'] = compraNormalizado
        item['venta'] = ventaNormalizado
        item['dia'] = datadia
        item['hora'] = datahora
        yield item
