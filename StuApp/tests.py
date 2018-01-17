from collections import ChainMap
import collections
value = ChainMap()
for list_num in range(1,13):
    li_list = list_num + 1
    value["tab%s"%(list_num)] = li_list
    value=value.new_child()#添加字典到集合
    value=value.parents#取出一个空字典
for list_num in range(1,13):
    li_list = list_num + 1
    value["tab%s"%(list_num)] = li_list
    value=value.new_child()#添加字典到集合
    value=value.parents#取出一个空字典
print(value)#打印合并后的字典
print(dict(value))#从对象中提取字典






