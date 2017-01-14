# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os
from dbtools import Dbtools

class QiubaiPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        # db = Dbtools('localhost','root','','qiubai')

        #获取数据
        qid = item['qid']
        headimg = item['headimg'][0]
        author = item['author'][0].encode('utf-8')
        content = item['content'][0].encode('utf-8')
        if item['thumb']:
            thumb = item['thumb'][0]
        else:
            thumb = ''
        upvote = item['upvote'][0]
        comment = item['comment'][0]

        #写入数据库
        db = Dbtools('localhost','root','','qiubai')
        result = db.execute('select * from hot where `qid` = '+ qid)
        if result <= 0:
            db = Dbtools('localhost','root','','qiubai')
            sql = 'insert into hot(`qid`, `author`, `headimg`, `content`, `thumb`, `upvote`, `comment`) values(%d, "%s", "%s", "%s", "%s", %d, %d)' %(int(qid), author, headimg, content, thumb, int(upvote), int(comment))
            db.execute(sql)

            #写入本地html中
            with open('qiubai.html', 'a') as file:
                html =  '<img src="%s" width="35" height="35">'%(headimg) + '作者：' + author + '&nbsp;&nbsp;&nbsp;&nbsp;' + upvote + '赞&nbsp;&nbsp;'+ comment + '评论&nbsp;&nbsp;' + '时间&nbsp;' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()) +'<br/>\t'
                html += '<p>\n\r'
                html += content + '<br>'
                html += '<img src="%s">'%(thumb)
                html += '</p>'
                html = '<p>%s</p>\n\r'%(html)
                file.write(html);

        return item
