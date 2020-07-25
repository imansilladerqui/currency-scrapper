import scrapy
import time
from scrapy.spiders import CrawlSpider
from vaccaroposadas.items import VaccaroposadasItem

class VaccaroSpider(CrawlSpider):
    name = 'vaccaroposadas'
    allowed_domains = ['fvaccaro.com']
    start_urls = ['http://www.fvaccaro.com/coti_section.asp']

    def parse(self, response):

        datadia = time.strftime("%d/%m/%Y")
        datahora = time.strftime("%H:%M:%S", time.localtime())
        compraDesdeLaWeb = response.xpath('//html/body/table[1]/tr[@class="modo1"]/td[1]/text()').extract_first()
        compraNormalizado = compraDesdeLaWeb.replace(u'\r\n\t\t\t    ', u'')
        ventaDesdeLaWeb = response.xpath('//html/body/table[1]/tr[@class="modo1"]/td[2]/text()').extract_first()
        ventaNormalizado = ventaDesdeLaWeb.replace(u'\r\n\t\t\t    ', u'')

        item = VaccaroposadasItem()
        item['entidad'] = 'Vaccaro'
        item['compra'] = compraNormalizado
        item['venta'] = ventaNormalizado
        item['dia'] = datadia
        item['hora'] = datahora
        yield item
