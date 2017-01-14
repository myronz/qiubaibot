# -*- coding: utf-8 -*-

#from dbtools import *
from dbtools import Dbtools

db = Dbtools('localhost','root','','qiubai')

sql = 'insert into hot(`author`, `headimg`, `content`, `thumb`, `upvote`, `comment`) values("test", "headimg", "这是一个内容", "这是头像", "10", "dddd")'
result = db.execute(sql)
print(result);