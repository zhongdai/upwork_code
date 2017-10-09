# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, TextResponse
import os



class ReviewSpider(scrapy.Spider):
    """The major spider class
    """
    name = 'review'
    allowed_domains = ['winereviewer.com.au']
    start_urls = ['http://winereviewer.com.au/search-for-a-review/search-results?keywords=Shiraz']

    def parse(self, response):
        """Parse the search result, get the URLs for each wine and the links to each page
        """
        for url in response.xpath('//div[@id="jr-listing-column"]/div[contains(@class,jr-layout-outer)]//a[starts-with(@id,"jr-listing-title")]/@href').extract():
            yield Request(url=response.urljoin(url), callback=self.parse_detail)

        for page_url in response.xpath('//div[@class="jrCol4 jrPagenavPages"]/a/@href').extract():
            yield Request(url=page_url, callback=self.parse)


    def parse_detail(self, response):
        """Parse the singl wine page, and return the result as dict
        """
        final_dict = {}
        name = response.xpath('//span[@itemprop="headline"]/text()').extract_first()
        pairs = response.xpath('//div[@class="jrFieldGroup wine-details1"]/div/div/text()').extract()
        for i in range(0,len(pairs),2):
            final_dict[pairs[i]] = pairs[i+1]

        final_dict['Name'] = name
        final_dict['Original_url'] = response.url

        final_dict['Web'] = response.xpath('//div[@class="jrListingFulltext "]/p/a/@href').extract_first()

        yield final_dict

    def parse_to_be_tested(self, response):
        """A simple dummy parser to be tested
        """
        url = response.url
        title = response.xpath('//div[@class="item1"]/text()').extract_first()

        return {
            'url': url,
            'title': title
        }
