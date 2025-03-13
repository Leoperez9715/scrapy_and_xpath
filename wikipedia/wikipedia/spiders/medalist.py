import scrapy


class MedalistSpider(scrapy.Spider):
    name = "medalist"
    allowed_domains = ["wikipedia.com"]
    start_urls = ["https://wikipedia.com"]

    def parse(self, response):
        pass
