# -*- coding: utf-8 -*-
import scrapy
from ..items import CourseItem

class ExpertzlabSpider(scrapy.Spider):
    name = 'expertzlab'
    allowed_domains = ['expertzlab.com']
    start_urls = ['http://expertzlab.com/']

    def parse(self, response):
        coursename = response.xpath('//div[@class="course"]/h4/text()').getall()
        desc = response.xpath('//div[@class="course"]/p/text()').getall()

        for x,y in zip (coursename, desc):
            course= CourseItem()
            course['name']= x
            course['desc']= y
            yield course