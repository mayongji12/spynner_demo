#__coding:utf-8__
#!/usr/bin/python
# File Name: totalphone.py
# Author: ma6174
# mail: ma6174@163.com
# Created Time: 2015年09月24日 星期四 12时41分47秒
#########################################################################
import spynner
import pyquery
import time
import BeautifulSoup
import sys,os
from PyQt4 import  QtWebKit
import urllib,urllib2

reload(sys)
sys.setdefaultencoding( "utf-8")
browser = spynner.Browser()
browser.create_webview()
browser.set_html_parser(pyquery.PyQuery)
browser.load("http://item.jd.com/1672050356.html#comments-list", 20)
 
try:
    browser.wait_load(10)
except:
    pass
string = browser.html
browser.close()
print 'string!'
soup = BeautifulSoup.BeautifulSoup(string)
time.sleep(2)
tags1 = soup.findAll('li',{"class":"ui-switchable-item trig-item"})
del tags1[2]
del tags1[0]
tag = []
for i in tags1:
    tag.append(i.contents)


def total_comment(tag):
    t_start = str(tag).find('inline;">(')
    t_stop = str(tag).find(')</em>')
    t_comment = str(tag)[t_start+10:t_stop]
    return t_comment

t = total_comment(tag[0])
#t_start = str(tag[0]).find('inline;">(')
#t_stop = str(tag[0]).find(')</em>')
#t_comment = str(tag[0])[t_start+10:t_stop]
#print t_comment

def part_comment(tag):
    g_start = str(tag).find('<em>(')
    g_stop = str(tag).find(')</em>')
    g_comment = str(tag)[g_start+5:g_stop]
    return g_comment

g = part_comment(tag[1])
m = part_comment(tag[2])
b = part_comment(tag[3])
x = str(int(g)*100/int(t))+'%'
print '''
    商品名称 ： 索尼(SONY) L55u Xperia Z3
    总评价   ： %s
    好评     ： %s
    中评     ： %s
    差评     ： %s
    好评率   :  %s

''' % (t,g,m,b,)
'''
print tag[1]
g_start = str(tag[1]).find('<em>(')
g_stop = str(tag[1]).find(')</em>')
g_comment = str(tag[1])[g_start+5:g_stop]
print g_comment


print tag[2]
m_start = str(tag[2]).find('<em>(')
m_stop = str(tag[2]).find(')</em>')
m_comment = str(tag[2])[m_start+5:m_stop]
print m_comment


print tag[3]
b_start = str(tag[3]).find('<em>(')
b_stop = str(tag[3]).find(')</em>')
b_comment = str(tag[3])[b_start+5:b_stop]
print b_comment
'''
#    else:
#    else:
#        print '+++++++++++++++++++++++++++++++'
#        print tag.contents
'''
for i in tags1:
#    if i.contents[0] and len(i.contests[0])>1:
    print len(i)
#    print 'i: ',i
    c = i.contents
    print 'c: ',c
    print type(c)
'''    
