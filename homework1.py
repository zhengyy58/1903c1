import requests
from lxml import etree
import os

a = os.getcwd()
os.mkdir("{}/wanghong".format(a))

for i in range(1,75):
    url = 'http://www.9000.com/WangHong/index/p/{}.html'.format(i)
    response = requests.get(url).content.decode('utf-8')
    path1 = etree.HTML(response)
    path2 = path1.xpath("//div[@class='index-hot-img']/a/@href")
    for ii in path2:
        new_url = 'http://www.9000.com'+ii
        response1 = requests.get(new_url).content.decode('utf-8')
        path3 = etree.HTML(response1)
        path4 = path3.xpath("//div[@class='homepage-infos']/p[@class='homepage-detail']/span[1]/text()")
        if path4[0] == "女":
            name = path3.xpath("//div[@class='homepage-infos']/h4/span[@class='f20']/text()")
            print(name)
            infomatiuon = path3.xpath("//div[@class='homepage-top']/div[@class='homepage-infos']//text()")
            image = path3.xpath("//div[@class='homepage-avatar']/img/@src")
            os.mkdir("{}/wanghong/{}".format(a, name))
            for v in image:
                image_url = "http://www.9000.com" + v
                image_response = requests.get(image_url)
                print(image_url)
                with open("{}/wanghong/{}/{}.jpg".format(a,name,name), mode='wb') as fw:
                    fw.write(image_response.content)
                with open("{}/wanghong/{}/{}.txt".format(a,name,name), mode="w",encoding='utf-8') as fe:
                    fe.writelines(infomatiuon)

        else:
            pass










