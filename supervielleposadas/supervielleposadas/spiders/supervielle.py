import scrapy
import time
from scrapy.spiders import CrawlSpider
from supervielleposadas.items import SupervielleposadasItem
from scrapy.http import Request

class SupervielleSpider(CrawlSpider):
    name = 'supervielleposadas'
    allowed_domains = ['personas.supervielle.com.ar']
    start_urls = ['https://personas.supervielle.com.ar/Pages/QuotesPanel/Quotes.aspx']

    def start_requests(self):
        yield Request(url = 'https://personas.supervielle.com.ar/Pages/QuotesPanel/Quotes.aspx', callback = self.parse)

    def parse(self, response):

        datadia = time.strftime("%d/%m/%Y")
        datahora = time.strftime("%H:%M:%S", time.localtime())
        compraNormalizada = response.xpath('//*[@id="gvCotizaciones"]/tr[2]/td[2]/font/text()').extract_first()
        ventaNormalizada = response.xpath('//*[@id="gvCotizaciones"]/tr[2]/td[3]/font/text()').extract_first()

        item = SupervielleposadasItem()
        item['entidad'] = 'Supervielle'
        item['compra'] = compraNormalizada.replace(',','.')
        item['venta'] = ventaNormalizada.replace(',','.')
        item['dia'] = datadia
        item['hora'] = datahora

        yield item
