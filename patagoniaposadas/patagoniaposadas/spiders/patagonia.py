import scrapy
import time
from scrapy.spiders import CrawlSpider
from patagoniaposadas.items import PatagoniaposadasItem

class PatagoniaSpider(CrawlSpider):
    name = 'patagoniaposadas'
    allowed_domains = ['ebankpersonas.bancopatagonia.com.ar']
    start_urls = ['https://ebankpersonas.bancopatagonia.com.ar/eBanking/usuarios/cotizacionMonedaExtranjera.htm']

    def parse(self, response):

        datadia = time.strftime("%d/%m/%Y")
        datahora = time.strftime("%H:%M:%S", time.localtime())
        compraDesdeLaWeb = response.xpath('//*[@id="principal"]/table/tbody/tr[1]/td[2]/text()').extract_first()
        compraNormalizado = compraDesdeLaWeb.replace(u'$\xa0', u'')
        ventaDesdeLaWeb = response.xpath('//*[@id="principal"]/table/tbody/tr[1]/td[3]/text()').extract_first()
        ventaNormalizado = ventaDesdeLaWeb.replace(u'$\xa0', u'')

        item = PatagoniaposadasItem()
        item['entidad'] = 'Patagonia'
        item['compra'] = compraNormalizado.replace(',','.')
        item['venta'] = ventaNormalizado.replace(',','.')
        item['dia'] = datadia
        item['hora'] = datahora
        yield item
