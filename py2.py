# _*_ coding:utf-8 _*_
# @Time     :16:51
# @Author   :zwl
# @Email    :
# @File     :py2.py
# @Software :PyCharm
from __future__ import division
'''
列表
字典
元组
'''
# 列表 任意对象的有序集合 可变长度
L1 = [1,2,3] + ['a','b','c']
for x in L1:
    print x
L2 = ['abc',['def','ghi']]
L2.append('b')
L2.extend([5,6,7])
print(L2)

# 字典 无序 键值对
d1 = {'name':'zwl','sex':'man','age':28}
print d1['name']
print len(d1)
print d1.has_key('name')
print d1.has_key('weigth')

# 元组 一旦创建 不可改变  有序
T=(1,2,3,4)
print T

myfile = open('a.txt')
print myfile.readline()
print myfile.readline()
myfile.close()
