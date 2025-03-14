import scrapy


class MedalistsSpider(scrapy.Spider):
    name = "medalists"
    allowed_domains = ["wikipedia.org"]
    start_urls = [r"https://es.wikipedia.org/wiki/Anexo:Pel%C3%ADculas_con_m%C3%A1s_premios_%C3%93scar"]

    def parse(self, response):
        pass
