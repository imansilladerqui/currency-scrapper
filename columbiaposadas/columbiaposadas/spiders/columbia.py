import scrapy
import json
import time
from scrapy.spiders import CrawlSpider
from columbiaposadas.items import ColumbiaposadasItem

class ColumbiaSpider(CrawlSpider):
    name = 'columbiaposadas'
    allowed_domains = ['secure.bancocolumbia.com.ar']
    start_urls = ['https://secure.bancocolumbia.com.ar/web/json/apps/getPrices.aspx']

    def parse(self, response):

        datadia = time.strftime("%d/%m/%Y")
        datahora = time.strftime("%H:%M:%S", time.localtime())
        response = json.loads(response.body)
        responseJsoncompra = response[0]['compra']
        responseJsonventa = response[0]['venta']

        compraDesdeLaWeb = str(responseJsoncompra)
        compraNormalizado = compraDesdeLaWeb[:-2]
        ventaDesdeLaWeb = str(responseJsonventa)
        ventaNormalizado = ventaDesdeLaWeb[:-2]

        item = ColumbiaposadasItem()
        item['entidad'] = 'Columbia'
        item['compra'] = compraNormalizado
        item['venta'] = ventaNormalizado
        item['dia'] = datadia
        item['hora'] = datahora
        yield item
