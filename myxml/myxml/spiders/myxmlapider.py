# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem


class MyxmlapiderSpider(XMLFeedSpider):
    name = 'myxmlapider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'rss' # change it accordingly

    def parse_node(self, response,node):
        i = MyxmlItem()
        i['title']=node.xpath("/rss/channel/item/title/text()").extract()
        i['link'] = node.xpath("/rss/channel/item/link/text()").extract()
        i['author'] = node.xpath("/rss/channel/item/author/text()").extract()
        for j in range(len(i["title"])):
            print(i['title'][j])
            print(i['link'][j])
            print(i['author'][j])
            print("------------------")
        return i
