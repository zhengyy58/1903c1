import threading,requests,re,sqlite3,queue

# class a(threading.Thread):
#     def __init__(self):
#         super().__init__()
#
#     def run(self):
#         print(1)
#
#
# class b(threading.Thread):
#     def __init__(self):
#         super().__init__()
#
#     def run(self):
#         print(2)
#
#
# if __name__ == "__main__":
#     A = a()
#     B = a()
#     C = b()
#     D = b()
#     A.start()
#     B.start()
#     C.start()
#     D.start()






class games(threading.Thread):
    def __init__(self,url,q):
        super().__init__()
        self.url = url
        self.q = q

    def run(self):
        r = requests.get(self.url)
        con = r.content.decode("utf-8")

        a = re.findall('</a>--><a href="(.*?)" tar.*?game-down">.*?</a></div>',con)
        for i in a:
            new_url = "https://down.ali213.net"+i
            new_r = requests.get(new_url)
            new_c = new_r.content.decode("utf-8")

            name = re.findall('<h1>(.*)</h1>',new_c)
            intro = re.findall('<p>.[\S\s]*</p>[\s]{7}</div>',new_c)
            # print(intro)
            intro1 = "".join(intro)
            a = re.sub("[^\u4e00-\u9fa5]","",intro1)

            self.q.put([name[0],a])
            print(name[0]+"存入成功")

            # print(self.q.get())

            break



class data(threading.Thread):
    def __init__(self,q):
        super().__init__()
        self.q = q

    def run(self):
        print(self.q.get())




if __name__ == "__main__":
    q = queue.Queue()
    url = "https://down.ali213.net/new/"
    G = games(url,q)
    D = data(q)
    G.start()
    D.start()







