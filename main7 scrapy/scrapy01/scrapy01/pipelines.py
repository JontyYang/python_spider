# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

#
# class Scrapy01Pipeline(object):
#     def __init__(self):
#         self.fp = open("duanzi.json", "w", encoding="utf-8")
#
#     def open_spider(self, spider):
#         print("爬虫kaishi了")
#
#     def process_item(self, item, spider):
#         item_json = json.dumps(item, ensure_ascii=False)
#         print(type(item))
#         print(item)
#         self.fp.write(item_json + '\n')
#         return item
#
#     def close_spider(self, spider):
#         self.fp.close()
#         print("爬虫结束了")



# 该方法是将所有返回内容加载至内存，之后一次写入，比较消耗内存
# from scrapy.exporters import JsonItemExporter
# class Scrapy01Pipeline(object):
#     # wb以二进制格式导入
#     def __init__(self):
#         self.fp = open("duanzi.json", "wb")
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
#         # 开始导出
#         self.exporter.start_exporting()
#
#
#     def open_spider(self, spider):
#         print("爬虫kaishi了")
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print("爬虫结束了")



# 一行一行写入
from scrapy.exporters import JsonLinesItemExporter
class Scrapy01Pipeline(object):
    # wb以二进制格式导入
    def __init__(self):
        self.fp = open("duanzi.json", "wb")
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')


    def open_spider(self, spider):
        print("爬虫kaishi了")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.fp.close()
        print("爬虫结束了")