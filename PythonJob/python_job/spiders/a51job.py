# -*- coding: utf-8 -*-
import scrapy

from python_job.items import PythonJobItem 


class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['m.51job.com']
    current_page = 1
    max_page = 2
    # 北京 = 010000
    start_urls = [
        'https://m.51job.com/search/joblist.php?jobarea=010000&keyword=python&keywordtype=2&pageno=1'
        ]
    custom_settings = {
        "ITEM_PIPELINES":{
            'python_job.pipelines.FiveJobPipeline': 300
        }
    }
    
    def parse(self, response):
        q = response.xpath
        items = q('//div[@class="items"]/a/@href').extract()
        for url in items:
            yield scrapy.Request(url, callback=self.parse_item)

        if self.current_page < self.max_page:
            self.current_page += 1
            next_page = 'https://m.51job.com/search/joblist.php?jobarea=010000&keyword=python&keywordtype=2&pageno=' + str(self.current_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_item(self, response):
        item =  PythonJobItem()
        q = response.xpath
        item['address'] = q('//div[@class="jt"]/em/text()').extract_first('北京')
        item['salary'] = q('//p[@class="jp"]/text()').extract_first('面议')
        item['create_time'] = q('//div[@class="jt"]/span//text()').extract_first() 
        item['postion_id'] = response.url.split("/")[-1].split('.')[0]
        item['position_name'] = q('//div[@class="jt"]/p/text()').extract_first()
        item['work_year'] = q('//span[@class="s_n"]/text()').extract_first('不限') 
        item['company_name'] = q('//p[@class="c_444"]/text()').extract_first()
        item['educational']  = q('//span[@class="s_x"]//text()').extract_first('不限') 
        item['body']  = q('//div[@class="ain"]/article//text()').extract()
        yield  item
