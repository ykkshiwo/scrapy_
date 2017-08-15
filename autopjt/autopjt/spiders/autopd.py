# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request

class AutopdSpider(scrapy.Spider):
    name = 'autopd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4002203.html']

    def parse(self, response):
        item=AutopjtItem()
        item["name"]=response.xpath("//a[@class='pic']").extract()
        item["price"]=response.xpath("//span[@class='price_n']/text()").extract()
        item["link"]=response.xpath("//a[@class='pic']/@href").extract()
        item["comnum"]=response.xpath("//a[@name='P_pl']/text()").extract()
        print(dict(item))
        '''yield item
        for i in range(1,76):
            url="http://category.dangdang.com/pg"+str(i)+"-cid4002203.html"
            yield Request(url,callback=self.parse)'''
