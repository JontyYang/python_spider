import json

__author__ = "Jonty yang"

# json 本质上是一个字符串


# 将python对象转换为json对象
# persons = [
#     {
#         'username': '李四',
#         'age': 23,
#         'country': 'chian'
#     },
#     {
#         'username': '张三',
#         'age': 43,
#         'country': 'china'
#     }
# ]
#
# # 字典和列表转json
# json_str = json.dumps(persons, ensure_ascii=False)
# print(json_str)
#
# # 将字典和列表以json形式写入文件
# with open('person.json', 'w', encoding="utf-8") as fp:
#     fp.write(json_str)
#     # json.dump(persons, fp, ensure_ascii=False)      # 将ensure_ascii 设置为true，显示汉字
#
# # 将一个json字符串转换为python对象
str = '[{"username": "李四", "age": 23, "country": "chian"}, {"username": "张三", "age": 43, "country": "china"}]'
person = json.loads(str)
print(type(person))
for per in person:
    print(per)
#
# # 将一个json文件中内容转换为python对象
# with open('person.json', 'r', encoding='utf-8') as fp:
#     personss = json.load(fp)
#     print(type(personss))
#     for pers in personss:
#         print(pers)

#    csv文件
# 将数据写入csv文件
import csv

def writer_demo1():
    # 表头信息
    headers = ['username', 'age', 'height']
    # 列表信息
    values = [
        ('张三', 18, 67),
        ('李四', 54, 67),
        ('王麻子', 20, 67)
    ]
    with open('1.csv', 'w', encoding='utf-8', newline='') as fp:  # newline指定每写入一行不换行
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(values)

def writer_demo2():
    # 表头信息
    headers = ['username', 'age', 'height']
    # 列表信息
    values = [
        {'username': '张三', 'age': 18, 'height': 180},
        {'username': '李四', 'age': 19, 'height': 181},
        {'username': '王五', 'age': 20, 'height': 182}
    ]
    with open('2.csv', 'w', encoding='utf-8', newline='') as fp:
        dictwriter = csv.DictWriter(fp, headers)
        # 写入表头数据的时候，需要调用writeheaders函数
        dictwriter.writeheader()
        dictwriter.writerows(values)



def reader_demo1():
    with open('1.csv', 'r', encoding='utf-8') as fp:
        # reader是迭代器
        reader = csv.reader(fp)
        next(reader)
        for x in reader:
            print(x)


def reader_demo2():
    with open('2.csv', 'r', encoding='utf-8') as fp:
        # dictreader返回为迭代器，内容为字典，不会包含标题
        dictreader = csv.DictReader(fp)
        for dic in dictreader:
            print(dic)



if __name__ == '__main__':
    # writer_demo1()
    # writer_demo2()
    # reader_demo1()
    reader_demo2()