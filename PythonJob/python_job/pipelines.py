# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FiveJobPipeline(object):
    def process_item(self, item, spider):
        length = len(item['body'])
        for i in range(length):
            item['body'][i] = item['body'][i].strip()
            item['body'][i] = ''.join(item['body'][i].split(' '))
            item['body'][i] = ''.join(item['body'][i].split('\xa0'))

        item['body'] = ''.join(item['body'])

        return item

class ZhiPinPipeline(object):
    def process_item(self, item, spider):
        length = len(item['body'])
        for i in range(length):
            item['body'][i] = item['body'][i].strip()

        item['body'] = ''.join(item['body'])

        item['salary'] = item['salary'].strip()
        item['company_name'] = item['company_name'].strip()
        return item

class ZhiLianPipeline(object):
    def process_item(self, item, spider):
        length = len(item['body'])
        for i in range(length):
            item['body'][i] = item['body'][i].strip()
            item['body'][i] = ''.join(item['body'][i].split(' '))

        item['body'] = ''.join(item['body'])

        item['work_year'] = item['work_year'].strip()
        item['educational'] = item['educational'].strip()
        return item




