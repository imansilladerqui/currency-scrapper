import scrapy
import time
from scrapy.spiders import CrawlSpider
from montevideoposadas.items import MontevideoposadasItem

class CambiomontevideoSpider(CrawlSpider):
    name = 'montevideoposadas'
    allowed_domains = ['montevideocambio.com.ar']
    start_urls = ['http://montevideocambio.com.ar/']

    def parse(self, response):

        datadia = time.strftime("%d/%m/%Y")
        datahora = time.strftime("%H:%M:%S", time.localtime())

        item = MontevideoposadasItem()
        item['entidad'] = 'Montevideo'
        item['compra'] = response.xpath('//*[@id="monedas"]/div[1]/div[1]/div[2]/text()').extract_first()
        item['venta'] = response.xpath('//*[@id="monedas"]/div[1]/div[1]/div[3]/text()').extract_first()
        item['dia'] = datadia
        item['hora'] = datahora
        yield item
