# coding=utf-8

import os
from unittest.case import TestCase
from winereview.spiders.review import ReviewSpider
from scrapy.http import Request, TextResponse

def fake_response(file_name=None, url=None):
    """Create a Scrapy fake HTTP response from a HTML file"""
    if not url:
        url = r'http://www.example.com'

    request = Request(url=url)
    if file_name:
        if not file_name[0] == '/':
            responses_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(responses_dir, file_name)
        else:
            file_path = file_name

        file_content = open(file_path, 'r').read()
    else:
        file_content = ''

    response = TextResponse(url=url, request=request, body=file_content,
                            encoding='utf-8')
    return response

class MyTestCase(TestCase):
    def setUp(self):
        self.spider = ReviewSpider()

    def test_parse(self):
        response = fake_response('input.html')
        item = self.spider.parse_to_be_tested(response)
        self.assertEqual(item['title'], 'My Title')
        self.assertEqual(item['url'], r'http://www.example.com')
