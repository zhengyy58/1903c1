import requests,re
#
# r = requests.get("http://www.waixie.net/treat/index.php")
# con = r.content.decode("utf-8")
#
# # print(type(con))
# tit = re.findall('<a href="(.*)" ta.*"STYLE22 STYLE9">.*</a>',con)
# # print(tit)
# for i in tit:
#     nuw_url=requests.get("http://www.waixie.net/treat/"+i).content.decode('utf-8')
#     a = re.findall('<div align="left".*>(.{5})</div>',nuw_url)
#     a1 = re.findall('<span class="STYLE[8-9]">(.*)</span>',nuw_url)
#     print(a,a1[0:4])

for i in range(0,4986):
    url = "http://www.waixie.net/task/index.php?pageNum_treat={}&totalRows_treat=74762".format(i)
    # print(url)STYLE22 STYLE9
    r =  requests.get(url).content.decode('utf-8')
    con =  re.findall('<a href="(.*)" ta.*class="STYLE22 STYLE9">.*</a>',r)
    for a in con:
        b ="http://www.waixie.net/task/"+ a
        # print(b)
        c =requests.get(b)
        d  = c.content.decode("utf-8")
        e = re.findall('<img src="(.*)" width="300" height="270" alt=".*".*>',d)
        for f in e:
            g ="http://www.waixie.net/task/"+f
            # print(g)
            h = requests.get("http://www.waixie.net/task/info.php?id=156774")
            h1= h.content.decode("utf-8")
            h2 = re.findall('<div align="left".*>(.*)</div>',h1)[0:4]
            h3= re.findall('<span class="STYLE[8,9]">(.*)</span>',h1)[0:4]

            # for h12,h13 in zip(h2,h3):
                # print(h12,h13)
            h4 = re.findall('<td zzz="{.*ArticleID}" .*class="STYLE13">(.*)</td>',h1)
            h14= ''.join(h4).replace("\r",'').replace('&nbsp;','').replace('<br>','')
            # print(h14)
            h5 = re.findall('<span class="STYLE37">(.*)</span>',h1)
            h6= re.findall('<span class="STYLE13">(.*)</span>',h1)
            # for h15,h16 in zip(h5,h6):
            #     print(h15,h16)
            h7 = re.findall('<div align="right".*>(.*)</div>',h1)[3:]
            # print(h7)
            h8 = re.findall('<span class=.*>(.*)</span>',h1)[11:14]  #邮箱

            h9 = re.findall('<td height="25".*>(.*)</td>',h1)[6:8]

            # for h17,h18 in zip(h7,h8):
            #     print(h17,h18)
            h10 = re.findall('<div .*class="STYLE19 STYLE35 STYLE36">(.*)</div>',h1)
            print(h10)
