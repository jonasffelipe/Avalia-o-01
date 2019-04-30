import scrapy
from scrapy.utils.response import open_in_browser

class YahooSpider(scrapy.Spider):

    name = 'Noticias_Yahoo'
    start_urls = {
        'https://br.noticias.yahoo.com/'
    }

    def parse(self, response):
        #open_in_browser(response)
        noticias = response.css('.js-stream-content')
        
        for manchete in noticias:
            print('Manchete: '+str(manchete.css('::text').extract_first()))