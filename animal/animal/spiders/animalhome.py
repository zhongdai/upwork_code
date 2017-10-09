# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class AnimalhomeSpider(scrapy.Spider):
    name = 'animalhome'
    allowed_domains = ['animalhome.es']
    start_urls = ['http://www.animalhome.es/perros-en-adopcion/']

    def parse(self, response):
        detail_urls = response.xpath('//div[@id="product_masonry"]/div/div/a/@href').extract()
        for url in detail_urls:
            yield Request(url=url, callback=self.parse_detail)

        page_urls = response.xpath('//ul[@class="page-numbers"]/li/a/@href').extract()
        for url in page_urls:
            yield Request(url=url, callback=self.parse)

    def parse_detail(self, response):
        return_dict = {}
        return_dict['url'] = response.url
        attrs = response.xpath('//table[@class="shop_attributes"]//tr/th/text()').extract()
        values = response.xpath('//table[@class="shop_attributes"]//tr/td/p/text()').extract()
        for key, value in zip(attrs, values):
            return_dict[key.strip()] = value.strip()
        image_urls = response.xpath('//div[@class="images kad-light-gallery"]//img/@src').extract()
        return_dict['image_urls'] = image_urls

        yield return_dict
