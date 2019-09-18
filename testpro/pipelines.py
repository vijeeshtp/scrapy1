# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TestproPipeline(object):
    def process_item(self, item, spider):
        return item
import re
from scrapy.exceptions import DropItem
class CoursePipeline(object):
    def process_item(self, item, spider):
        desc= item.get('desc')
        res = re.findall("Python",desc)
        if len(res) > 0 :
            return item
        else :
            raise DropItem("Missing python")