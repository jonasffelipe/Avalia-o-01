import scrapy
from scrapy.utils.response import open_in_browser

class MLSpider(scrapy.Spider):

    name = 'Preço Mercado Livre'

    produto = 'tenis'

    start_urls = {
        'https://lista.mercadolivre.com.br/{}'.format(produto)
    }
    
    def parse(self, response):
        #open_in_browser(response)
        #produtos = response.css('.price__fraction , .main-title')
        produtos = response.css('.item__info')
        
        for produto in produtos:
            precos = produto.css('.price__fraction')
            descricao = produto.css('.main-title')
            #print(str(descricao.css('::text').extract_first()+' custa R$'+str(precos.css('::text').extract_first()))
            print('Produto: '+str(descricao.css('::text').extract_first()))
            print('Valor: R$'+str(precos.css('::text').extract_first()))