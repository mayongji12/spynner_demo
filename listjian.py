#__coding:utf-8__
#!/usr/bin/python
# File Name: listjian.py
# Author: ma6174
# mail: ma6174@163.com
# Created Time: 2015年10月11日 星期日 07时44分21秒
#########################################################################
list1 = [9,5,4,1,6,8,9]
list2 = []
for i in range(len(list1)):
    if i+1 - len(list1):
        list2.append(list1[i]-list1[i+1])
print "list1: " ,list1
print "list2: " ,list2
