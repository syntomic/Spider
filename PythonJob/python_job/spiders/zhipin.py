# -*- coding: utf-8 -*-
import scrapy
import json

from python_job.items import PythonJobItem 

class ZhipinSpider(scrapy.Spider):
    name = 'zhipin'
    allowed_domains = ['www.zhipin.com']
    current_page = 1
    max_page = 2
    start_urls = [
            'https://www.zhipin.com/c101010100/?query=python'
    ]
    custom_settings ={
        "DEFAULT_REQUEST_HEADERS":{
            'host': "www.zhipin.com",
            'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            'accept-language': "en-US,en;q=0.5",
            'accept-encoding': "gzip, deflate, br",
        },
        "ITEM_PIPELINES":{
            'python_job.pipelines.ZhiPinPipeline': 300
        }
    }

    def parse(self, response):
        q = response.xpath
        urls = q('//div[@class="info-primary"]//a/@href').extract()
        for url in urls:
            full_url = 'https://www.zhipin.com' + url
            yield scrapy.Request(full_url, callback=self.parse_item)

        if self.current_page < self.max_page:
            self.current_page += 1
            next_page = 'https://www.zhipin.com/c100010000/?query=python&page={}'.format(self.current_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_item(self,response):
        item = PythonJobItem()
        q = response.xpath
        item['address'] = q('/html/body/div[1]/div[2]/div[1]/div/div/div[2]/p/text()').extract_first()
        item['work_year'] = q('/html/body/div[1]/div[2]/div[1]/div/div/div[2]/p/text()').extract()[1]
        item['educational'] = q('/html/body/div[1]/div[2]/div[1]/div/div/div[2]/p/text()').extract()[2]
        item['salary'] = q('//span[@class="salary"]/text()').extract_first() 
        item['company_name'] = q('/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/text()').extract_first()
        item['postion_id'] = response.url.split("/")[-1].split('.')[0]
        item['position_name'] = q('//*[@id="main"]/div[2]/div/div[2]/div[1]/h1/text()').extract_first()
        item['body']  = q('//div[1]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/text()').extract()
        yield  item
