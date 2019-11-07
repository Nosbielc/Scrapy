import scrapy
# from scrapy.cmdline import execute
# execute()

class UolSpider(scrapy.Spider):
    name = 'uol'
    start_urls = ['https://www.uol.com.br/']

    def parse(self, response):
        self.log('Hello Word')
        self.log(response.body)

