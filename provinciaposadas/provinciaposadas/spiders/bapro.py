import scrapy
import json
import time
from scrapy.spiders import CrawlSpider
from provinciaposadas.items import ProvinciaposadasItem

class BaproSpider(CrawlSpider):
    name = 'provinciaposadas'
    allowed_domains = ['bancoprovincia.com.ar']
    start_urls = ['https://www.bancoprovincia.com.ar/Principal/Dolar']

    def parse(self, response):

        datadia = time.strftime("%d/%m/%Y")
        datahora = time.strftime("%H:%M:%S", time.localtime())
        response = json.loads(response.body_as_unicode())
        responseJsoncompra = response[0]
        responseJsonventa = response[1]

        compraDesdeLaWeb = responseJsoncompra
        compraNormalizado = compraDesdeLaWeb[:-1]
        ventaDesdeLaWeb = responseJsonventa
        ventaNormalizado = ventaDesdeLaWeb[:-1]

        item = ProvinciaposadasItem()
        item['entidad'] = 'Bapro'
        item['compra'] = compraNormalizado
        item['venta'] = ventaNormalizado
        item['dia'] = datadia
        item['hora'] = datahora
        yield item
