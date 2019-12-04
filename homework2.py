import requests,os
from lxml import etree

e = os.getcwd()
print(e)
url ="http://www.jokeji.cn/list.htm"
a = requests.get(url).content.decode('gbk')
b = etree.HTML(a)
c = b.xpath("//div[@class='joke_right']/ul/li/a/@href")
for i in c:
    url1="http://www.jokeji.cn/"
    url2=url1+i
    aa = requests.get(url2).content.decode('gbk')
    bb = etree.HTML(aa)
    cc = bb.xpath("//div[@class='list_title']/ul/li/b/a/@href")
    for v in cc:
        vv = "http://www.jokeji.cn"
        url3=vv+v
        aaa = requests.get(url3).content.decode('gbk')
        bbb = etree.HTML(aaa)
        ccc = bbb.xpath("//div[@class='left_up']/ul/span[@id='text110']/p/text()")
        print(ccc)
        with open('笑话.txt',"a")as n:
            n.write(str(ccc))