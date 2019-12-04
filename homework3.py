import requests
from lxml import etree
import os


def content_x(url, way):
    response = requests.get(url)
    content = response.content.decode(way)
    content_xx = etree.HTML(content)
    return content_xx


# 获得主页面url
for i in range(34, 41):
    url_c = "http://www.congwen.net/"+"/Art.asp?c_id={}".format(i)
    detail = content_x(url_c, "gbk")
    urls_d = detail.xpath("//table//tr/td/table//tr/td/div[1]/div[1]/a/@href")
    for a in urls_d:
        url_t = "http://www.congwen.net//" + a
        detail_f = content_x(url_t, "gbk")
        urls_t = detail_f.xpath("//table//tr/td[1]/a/@href")[0:10]
        for b in urls_t:
            url_s = "http://www.congwen.net" + b
            detail_s = content_x(url_s, "gbk")
            text_title = detail_s.xpath("//table//tr[1]/td/h2/text()")
            text_time = detail_s.xpath("//div[@class='conl']/table//tr[2]/td/p[1]/text()")
            text_detail = detail_s.xpath("//div[@class='conl']/table//tr[3]/td[@id='con']/text()")
            title = "".join(text_title)
            time = "".join(text_time)
            text_con = "".join(text_detail)
            print(title)
            print(time)
            print(text_con)

            """
            //div[@class='conl']/table/tbody/tr[3]/td[@id='con']/text()
            """


