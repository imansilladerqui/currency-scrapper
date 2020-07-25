import scrapy
import time
from scrapy.spiders import CrawlSpider
from francesposadas.items import FrancesposadasItem


class FrancesSpider(CrawlSpider):
    name = 'francesposadas'
    allowed_domains = ['hb.bbv.com.ar']
    start_urls = ['https://hb.bbv.com.ar/fnet/mod/inversiones/NL-dolareuro.jsp']

    def parse(self, response):

        datadia = time.strftime("%d/%m/%Y")
        datahora = time.strftime("%H:%M:%S", time.localtime())
        compraDesdeLaWeb = response.xpath('//html/body/table/tr[1]/td[2]/span[@class="detalles"]/text()').extract_first()
        compraNormalizado = compraDesdeLaWeb[:-3]
        ventaDesdeLaWeb = response.xpath('//html/body/table/tr[1]/td[3]/span[@class="detalles"]/text()').extract_first()
        ventaNormalizado = ventaDesdeLaWeb[:-3]

        item = FrancesposadasItem()
        item['entidad'] = 'Frances'
        item['compra'] = compraNormalizado.replace(',','.')
        item['venta'] = ventaNormalizado.replace(',','.')
        item['dia'] = datadia
        item['hora'] = datahora
        yield item
