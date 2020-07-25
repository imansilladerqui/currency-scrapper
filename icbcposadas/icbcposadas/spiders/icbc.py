import scrapy
import json
import time
from scrapy.spiders import CrawlSpider
from icbcposadas.items import IcbcposadasItem

class IcbcSpider(CrawlSpider):
    name = 'icbcposadas'
    allowed_domains = ['icbc.com.ar']
    start_urls = ['https://www.icbc.com.ar/ICBC_CotizacionMonedaWEB/cotizacion/dolar']

    def parse(self, response):

        datadia = time.strftime("%d/%m/%Y")
        datahora = time.strftime("%H:%M:%S", time.localtime())
        response = json.loads(response.body)
        responseJsoncompra = response['valorCompra']
        responseJsonventa = response['valorVenta']

        compraDesdeLaWeb = responseJsoncompra
        compraNormalizado = compraDesdeLaWeb[:-2]
        ventaDesdeLaWeb = responseJsonventa
        ventaNormalizado = ventaDesdeLaWeb[:-2]

        item = IcbcposadasItem()
        item['entidad'] = 'ICBC'
        item['compra'] = compraNormalizado.replace(',','.')
        item['venta'] = ventaNormalizado.replace(',','.')
        item['dia'] = datadia
        item['hora'] = datahora
        yield item
