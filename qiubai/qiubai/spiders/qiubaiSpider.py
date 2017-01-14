#-*- coding: UTF-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from qiubai.items import QiubaiItem

class qiubaiSpider(scrapy.Spider):
    name = "qiubai"
    allowed_domains = ['http://www.qiushibaike.com']
    start_urls = [
        'http://www.qiushibaike.com/hot'
    ]

    def parse(self, response):
        for article in response.xpath('//div[@id="content-left"]/div[@class="article block untagged mb15"]'):
            item = QiubaiItem()

            #文章id
            qid_element = article.xpath('./a[@class="contentHerf"]/@href').extract()
            qid_data = qid_element[0].split('/')
            item['qid'] = qid_data[2]

            author_block =  article.xpath('./div[contains(@class, "author")]')      #用户块

            # 用户头像
            headimg = author_block.xpath('./a[1]/img/@src').extract()
            if headimg:
                item['headimg'] = headimg
            else:
                #匿名用户头像
                item['headimg'] = 'http://www.qiushibaike.com/static/images/thumb/anony.png?v=b61e7f5162d14b7c0d5f419cd6649c87'
           
            # 用户名称
            author = author_block.xpath('./a[2]/h2/text()').extract()
            if author:
                item['author'] = author
            else:
                item['author'] = '匿名用户'
            
            # 内容
            item['content'] = article.xpath('./a[@class="contentHerf"]/div[@class="content"]/span/descendant::text()').extract();
            
            #图片
            item['thumb'] = article.xpath('./div[@class="thumb"]/a/img/@src').extract()

            #点赞
            item['upvote'] = article.xpath('./div[@class="stats"]/span[@class="stats-vote"]/i/text()').extract()

            #评论数
            item['comment'] = article.xpath('./div[@class="stats"]/span[@class="stats-comments"]/a/i/text()').extract()

            yield item

        #获得下一篇文章的url

        #当前页码
        current_sel = response.xpath('//div[@id="content-left"]/ul[@class="pagination"]/li/span[@class="current"]/text()').extract()
        current = current_sel[0].strip()

        #下一页链接
        next_query_string = response.xpath('//div[@id="content-left"]/ul[@class="pagination"]/li/span[@class="current"]/parent::li/following-sibling::li[1]/a/@href').extract()
        next_url = 'http://www.qiushibaike.com' + next_query_string[0]

        #总共抓取1到第n页
        n = 5
        if int(current) < int(n):
            print('************')
            print('共抓取 %s 页，现在是第 %s 页' %(n, current))
            print('************')
            yield scrapy.Request(next_url, callback = self.parse, dont_filter = True)

        