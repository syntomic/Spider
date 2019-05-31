# -*- coding: utf-8 -*-
import scrapy

from python_job.items import PythonJobItem


class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['m.zhaopin.com']
    current_page = 1
    max_page = 5
    
    start_urls = [
        'https://m.zhaopin.com/beijing-530/?keyword=python&order=0&islocation=0&maprange=3'
    ]

    custom_settings ={
        "DEFAULT_REQUEST_HEADERS":{
            'host': "m.zhaopin.com",
            'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            'accept-language': "en-US,en;q=0.5",
            'accept-encoding': "gzip, deflate, br",
        },
        "ITEM_PIPELINES":{
            'python_job.pipelines.ZhiLianPipeline': 300
        }
    }

    def parse(self, response):
        q = response.xpath
        urls = q('//a[@class="boxsizing"]/@data-link').extract()
        for url in urls:
            complete_url = 'https://m.zhaopin.com' + url
            yield scrapy.Request(complete_url, callback=self.parse_item)

        if self.current_page < self.max_page:
            self.current_page += 1
            next_page = 'https://m.zhaopin.com/beijing-530/?keyword=python&pageindex={}&maprange=3&islocation=0&order=0'.format(self.current_page)
            yield scrapy.Request(next_page, callback=self.parse)

    # 尽量用属性选择
    def parse_item(self, response):
        q = response.xpath
        item = PythonJobItem()
        item['address'] = q('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[1]/text()').extract_first('北京')
        item['salary'] = q('//*[@id="r_content"]/div[1]/div/div[1]/div[1]/div[1]/text()').extract_first('面议')
        item['create_time'] = q('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[2]/text()').extract_first()
        item['company_name'] = q('//*[@id="r_content"]/div[1]/div/div[1]/div[2]/text()').extract_first()
        item['postion_id'] = response.url.split("/")[-2].split('.')[0]
        item['position_name'] = q('//*[@id="r_content"]/div[1]/div/div[1]/div[1]/h1/text()').extract_first()
        item['work_year'] = q('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[2]/text()').extract_first('不限') 
        item['educational']  = q('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[3]/text()').extract_first('不限')
        item['body']  = q('//*[@id="r_content"]/div[1]/div/article/div//text()').extract()
        yield item
