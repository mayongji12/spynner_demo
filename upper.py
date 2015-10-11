#__coding:utf-8__
#!/usr/bin/python
# File Name: upper.py
# Author: ma6174
# mail: ma6174@163.com
# Created Time: 2015年10月11日 星期日 03时44分18秒
#########################################################################
def capitalize_a(s):
    res = []
    for i in s:
        res1=[]
        for j in i:
            res1.append(j.capitalize())
        res.append(''.join(res1))    
    return res


