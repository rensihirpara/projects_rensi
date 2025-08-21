import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
