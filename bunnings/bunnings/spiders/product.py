# -*- coding: utf-8 -*-
import scrapy


class ProductSpider(scrapy.Spider):
    name = 'product'
    allowed_domains = ['bunnings.com.au']
    start_urls = ['http://bunnings.com.au/']

    def parse(self, response):
        pass
