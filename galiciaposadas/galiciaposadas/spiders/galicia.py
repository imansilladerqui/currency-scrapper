import scrapy
import json
import time
from scrapy.spiders import CrawlSpider
from galiciaposadas.items import GaliciaposadasItem


class GaliciaSpider(CrawlSpider):
    name = 'galiciaposadas'
    allowed_domains = ['bancogalicia.com']
    start_urls = ['https://www.bancogalicia.com/cotizacion/cotizar?currencyId=02&quoteType=SU&quoteId=999']

    def parse(self, response):

        datadia = time.strftime("%d/%m/%Y")
        datahora = time.strftime("%H:%M:%S", time.localtime())
        response = json.loads(response.body_as_unicode())
        responseJsoncompra = response["buy"]
        responseJsonventa = response["sell"]

        item = GaliciaposadasItem()
        item['entidad'] = 'Galicia'
        item['compra'] = responseJsoncompra.replace(',','.')
        item['venta'] = responseJsonventa.replace(',','.')
        item['dia'] = datadia
        item['hora'] = datahora
        yield item
