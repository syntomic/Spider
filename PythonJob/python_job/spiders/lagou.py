# -*- coding: utf-8 -*-
import scrapy
import json
import time

from python_job.items import PythonJobItem

class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['m.lagou.com']
    current_page = 1
    max_page = 20

    start_urls = [
        'https://m.lagou.com/search.json?city=全国&positionName=python&pageNo=1&pageSize=15'
    ]

    def parse(self, response):
        js = json.loads(response.body)
        #total = js['content']['data']['page']['totalCount']
        items = js['content']['data']['page']['result']

        for item in items:
            url = 'https://m.lagou.com/jobs/' + str(item['positionId']) + ".html"
            time.sleep(3)

            yield scrapy.Request(url, callback=self.parse_item, meta=item)

        if self.current_page < 4:
            self.current_page += 1
            next_page = 'https://m.lagou.com/search.json?city=全国&positionName=python&pageNo={}&pageSize=15'.format(str(self.current_page))
            time.sleep()
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_item(self, response):
        item = PythonJobItem()
        q = response.xpath
        #body = response.body.decode("utf-8")
        item['address'] = response.meta['city']
        item['salary'] = response.meta['salary']
        item['create_time'] = response.meta['createTime']
        item['body'] = q('//div[@class="content"]/p/text()').extract()
        item['company_name'] = response.meta['companyName']
        item['position_id'] = response.meta['positionId']
        item['position_name'] = response.meta['positionName']

        


