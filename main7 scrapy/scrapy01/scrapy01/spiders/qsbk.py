# -*- coding: utf-8 -*-
import scrapy

class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_url = 'https://www.qiushibaike.com'

    def parse(self, response):
        duanzidivs = response.xpath("//div[@class='col1 old-style-col1']/div")
        # 返回解析后的数据给pipelines
        for duanzidiv in duanzidivs:
            author = duanzidiv.xpath(".//h2/text()").get().strip()
            content = duanzidiv.xpath(".//span/text()").get().strip()
            # print(author)
            # print(content)
            duanzi = {'author': author, 'content': content}
            yield duanzi
        # 请求下一页
        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_url:
            return
        else:
            # 回调parse函数
            yield scrapy.Request(self.base_url+next_url, callback=self.parse)



