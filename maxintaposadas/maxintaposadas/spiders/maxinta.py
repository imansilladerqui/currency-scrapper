import scrapy
import time
from scrapy.spiders import CrawlSpider
from maxintaposadas.items import MaxintaposadasItem
from scrapy.http import Request

class MaxintaSpider(scrapy.Spider):
    name = 'maxintaposadas'
    allowed_domains = ['maxinta.com']
    start_urls = ['http://maxinta.com/']

    def start_requests(self):
        cookies = {
            'PHPSESSID':'75dvekebjto2btmsooaf32drq6',
            '_ga':'GA1.2.1480429770.1538354711',
            '_gid':'GA1.2.194624003.1538354711',
            '_gat':'1',
            }

        yield Request(url = 'http://maxinta.com/', callback = self.parse, cookies=cookies)

    def parse(self, response):

        datadia = time.strftime("%d/%m/%Y")
        datahora = time.strftime("%H:%M:%S", time.localtime())
        compraDesdeLaWeb = response.xpath('//div[@class="cotizaciones"]/table/tbody/tr/td[3]/text()').extract_first()
        compraNormalizado = compraDesdeLaWeb.replace(u'$ ', u'')
        ventaDesdeLaWeb = response.xpath('//div[@class="cotizaciones"]/table/tbody/tr/td[4]/text()').extract_first()
        ventaNormalizado = ventaDesdeLaWeb.replace(u'$ ', u'')

        item = MaxintaposadasItem()
        item['entidad'] = 'Maxinta'
        item['compra'] = compraNormalizado
        item['venta'] = ventaNormalizado
        item['dia'] = datadia
        item['hora'] = datahora
        yield item
