import scrapy
from scrapy.utils.response import open_in_browser

class YahooSpider(scrapy.Spider):

    name = 'Cotação do Dolar'
    start_urls = {
        'https://www.uol.com.br/'
    }

    def parse(self, response):
        #open_in_browser(response)
        cotacao = response.css('.currency_quote__down')
        
        for dolar in cotacao:
            print('\n')
            print('A cotação atual do dólar é: '+str(dolar.css('::text').extract_first()))
            print('\n')