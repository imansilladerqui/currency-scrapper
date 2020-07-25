import scrapy
import time
from scrapy.spiders import CrawlSpider
from alpeposadas.items import AlpeposadasItem

class CambioalpeSpider(CrawlSpider):
    name = 'alpeposadas'
    allowed_domains = ['cambioalpe.com.ar']
    start_urls = ['http://cambioalpe.com.ar/']

    def parse(self, response):

        datadia = time.strftime("%d/%m/%Y")
        datahora = time.strftime("%H:%M:%S", time.localtime())
        compraDesdeLaWeb = response.xpath('//*[@id="monedas"]/table/tbody/tr[1]/td[2]/text()').extract_first()
        compraNormalizado = compraDesdeLaWeb.replace(u'$  ', u'')
        ventaDesdeLaWeb = response.xpath('//*[@id="monedas"]/table/tbody/tr[1]/td[3]/text()').extract_first()
        ventaNormalizado = ventaDesdeLaWeb.replace(u'$  ', u'')


        item = AlpeposadasItem()
        item['entidad'] = 'Alpe'
        item['compra'] = compraNormalizado
        item['venta'] = ventaNormalizado
        item['dia'] = datadia
        item['hora'] = datahora
        yield item

