# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request, FormRequest
from PIL import Image

class LoginspdSpider(scrapy.Spider):
    name = 'loginspd'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def start_requests(self):
        print("start_1")
        return [Request("https://accounts.douban.com/login", meta={"cookiejar": 1}, callback=self.parse)]

    def parse(self, response):
        print("start_2")
        captcha = response.xpath('//img[@id="captcha_image"]/@src').extract()
        print(captcha)
        if len(captcha):
            print("有验证码，请仔细填写。")
            localpath = "e:/mypython/myscrapy/yzm.png"
            urllib.request.urlretrieve(captcha[0], filename=localpath)
            im = Image.open(localpath)
            im.show()
            print("请输入图片中的验证码：")
            captcha_value = input()
            print("你输入为： " + captcha_value)
            data = {
                "form_email": "452306233@qq.com",
                "form_password": "a199407311",
                "captcha-solution": captcha_value,
                "redir": "https://www.douban.com/people/165929360/",

            }
        else:
            print("没有验证码。")
            data = {
                "form_email": "452306233@qq.com",
                "form_password": "a199407311",
                #"captcha-solution": captcha_value,
                "redir": "https://www.douban.com/people/165929360/",

            }
            print("登入中...")
        return [FormRequest.from_response(response, formdata=data, callback=self.next)]

    def next(self, response):

        print("已经登入")
        print(response.xpath("//title/text()").extract()[0])
