import scrapy
import time
from scrapy.spiders import CrawlSpider
from santanderposadas.items import SantanderposadasItem

class SantanderSpider(CrawlSpider):
    name = 'santanderposadas'
    allowed_domains = ['banco.santanderrio.com.ar']
    start_urls = ['http://banco.santanderrio.com.ar/exec/cotizacion/index.jsp']

    def parse(self, response):

        datadia = time.strftime("%d/%m/%Y")
        datahora = time.strftime("%H:%M:%S", time.localtime())
        compraDesdeLaWeb = response.xpath('//*[@id="wrapper_new"]/main/article/div/div/table/tr[2]/td[2]/text()').extract_first()
        compraNormalizado = compraDesdeLaWeb.replace(u'$ ', u'')
        ventaDesdeLaWeb = response.xpath('//*[@id="wrapper_new"]/main/article/div/div/table/tr[2]/td[3]/text()').extract_first()
        ventaNormalizado = ventaDesdeLaWeb.replace(u'$ ', u'')
        if (compraDesdeLaWeb != '$ null' or ventaDesdeLaWeb != '$ null') :
            item = SantanderposadasItem()
            item['entidad'] = 'Santander'
            item['compra'] = compraNormalizado.replace(',','.')
            item['venta'] = ventaNormalizado.replace(',','.')
            item['dia'] = datadia
            item['hora'] = datahora
            yield item
