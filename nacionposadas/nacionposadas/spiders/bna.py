import scrapy
import time
from scrapy.spiders import CrawlSpider
from nacionposadas.items import NacionposadasItem

class BnaSpider(CrawlSpider):
    name = 'nacionposadas'
    allowed_domains = ['bna.com.ar']
    start_urls = ['http://www.bna.com.ar/Personas']

    def parse(self, response):

        datadia = time.strftime("%d/%m/%Y")
        datahora = time.strftime("%H:%M:%S", time.localtime())
        compraDesdeLaWeb = response.xpath('//*[@id="billetes"]/table/tbody/tr[1]/td[2]/text()').extract_first()
        compraNormalizado = compraDesdeLaWeb[:-2]
        ventaDesdeLaWeb = response.xpath('//*[@id="billetes"]/table/tbody/tr[1]/td[3]/text()').extract_first()
        ventaNormalizado = ventaDesdeLaWeb[:-2]

        item = NacionposadasItem()
        item['entidad'] = 'Nacion'
        item['compra'] = compraNormalizado.replace(',','.')
        item['venta'] = ventaNormalizado.replace(',','.')
        item['dia'] = datadia
        item['hora'] = datahora
        yield item
