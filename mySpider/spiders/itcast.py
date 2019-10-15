# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    # allowed_domains = ['www.itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        teacher_list = response.xpath('/html/body/div[1]/div[5]/div[2]/div[3]')
        for i in teacher_list:
            item = MyspiderItem()
            name = i.xpath("./ul/li[1]/div[2]/h3/text()").extract_first()
            item["name"] = name
            print(name)
            print("*"*50)

            yield item




