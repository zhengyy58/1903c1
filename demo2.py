from lxml import etree
import requests

for o in range(1,81):
    url = "http://www.iltaw.com/animal/all?page=%d" %o

    r = requests.get(url)
    html = r.content.decode("utf-8")

    con = etree.HTML(html)
    a = con.xpath("//div[@class='text-wrap']/h3/a/@href")
    for i in a:
        print(i)
        # new_r = requests.get(i)
        # new_h = new_r.content.decode("utf-8")
        #
        # new_c = etree.HTML(new_h)
        # b = new_c.xpath("//div[@class='property']/text()")
        # # print(b)
        # c = "".join(b)
        #
        # print(c.replace("\xa0","").replace(" ",""))

        with open('动物世界.txt','a+') as f:
            f.write(i)
            f.write("\n")

