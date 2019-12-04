import  requests

# header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
# inp = {"wd":"中国"}
#
# r = requests.get("https://www.baidu.com",headers=header,params=inp)
# # print(r.text)
# # print(r.content)
# a = r.content.decode("utf-8")
# # print(a)
# print(r.url)


url = 'http://httpbin.org/post'

data = {"name":"1903c"}

r = requests.post(url=url,data=data)
print(r.text)



