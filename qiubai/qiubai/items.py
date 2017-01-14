# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiubaiItem(scrapy.Item):
    # define the fields for your item here like:
    qid = scrapy.Field()        #文章id
    headimg = scrapy.Field()    #头像
    author = scrapy.Field()     #用户名
    content = scrapy.Field()    #内容
    thumb = scrapy.Field()      #图片
    upvote = scrapy.Field()     #点赞
    comment = scrapy.Field()    #评论
    pass
