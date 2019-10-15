# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MyspiderPipeline(object):
    def __init__(self):
        self.filename = open("teacher.json", "a")

    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False) + ",100"
        jsontext1 = json.dumps("100")
        self.filename.write(jsontext)
        # self.filename.write(jsontext1)
        print(jsontext)
        print("%" * 50)

        return item

    def close_spider(self, spider):
        self.filename.close()
