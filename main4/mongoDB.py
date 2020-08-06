__author__ = 'Jonty yang'

import pymongo

# Mongodb 基本操作命令
# db 查看当前数据库
# show dbs 查看所有数据库
# use 数据库名 使用数据库，如果不存在，会新创
# db.dropDatabase()   删除当前数据库
# db.集合名.insert() 添加数据到指定集合
# db.集合名.find() 从指定集合中查找数据

# 连接mongodb
# 获取连接mongodb的对象
client = pymongo.MongoClient('127.0.0.1', port=27017)
# 获取数据库(如果没有，则回新建，在内存中产生）
db = client.zhihu
# 获取集合
collection = db.qa
# 写入数据
# collection.insert_one({'username': "张三"})
# collection.insert_many([
#     {'username': 'aaa',
#      'age': 18
#      },
#     {'username': 'bbb',
#      'age': 19
#      }
# ])

# 查找数据
cursor = collection.find()    #迭代对象，获取所有数据
print(type(cursor))
for cur in cursor:
    print(cur)
# 获取集合中第一条数据,指定条件
result = collection.find_one({'age': 18})
print(result)

# 更新一条数据，指定条件,update_many为更新多条
collection.update_one({'username': 'aaa'}, {'$set': {'username': 'ccc'}})
collection.delete_one({'username': 'aaa'})

