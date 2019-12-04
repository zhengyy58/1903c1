import threading
import queue,requests,sqlite3
from lxml import etree

# class a(threading.Thread):
#     def __init__(self,date,q):
#         super().__init__()
#         self.date = date
#         self.q = q
#
#     def run(self):
#         print("这是线程a里的内容")
#         # print(self.date)
#         self.q.put(self.date)
#         print("存入成功")
#
#
# class b(threading.Thread):
#     def __init__(self,date,q):
#         super().__init__()
#         self.date = date
#         self.q = q
#
#     def run(self):
#         print("这是线程b里的内容")
#         # print(self.date)
#         print(self.q.get())
#         print("取出成功")
#
#
#
# if __name__ =="__main__":
#
#     num = 1
#     q = queue.Queue()
#
#     A = a(num,q)
#     B = b(num,q)
#     # A.start()
#     B.start()





# class zoo(threading.Thread):
#     def __init__(self,url,q):
#         super().__init__()
#         self.url = url
#         self.q = q
#
#     def run(self):
#         r = requests.get(self.url)
#         html = r.content.decode("utf-8")
#         con = etree.HTML(html)
#
#         name = con.xpath("//li[@class='clearfix']/div[@class='text-wrap']/h3/a/text()")
#         for i in name[::2]:
#             self.q.put(i)
#             print(i+"存入成功")
#
#         # print(len(name))
#         # a = 0
#         # for i in name:
#         #     a += 1
#         #     if a % 2 == 0:
#         #         # print("偶数")
#         #         b = name[a-2] + name[a-1]
#         #         print(b)
#         #
#         #     else:
#         #         # print("奇数")
#         #         # print(name[a-1])
#         #         pass
#
#
#
# class data(threading.Thread):
#     def __init__(self,q):
#         super().__init__()
#         self.q = q
#
#     def run(self):
#         print("消费者开始执行")
#         print(self.q.empty())
#         # while not self.q.empty():
#         #     a = self.q.get()
#         #     print(a)
#         while True:
#             try:
#                 print(self.q.get(timeout=5)+"取出成功")
#             except Exception:
#                 print("全部取出")
#                 break
#
#
#
#
#
#
#
# if __name__ == "__main__":
#     q = queue.Queue()
#
#     url = "http://www.iltaw.com/animal/all"
#
#     Z = zoo(url,q)
#     D = data(q)
#     Z.start()
#     D.start()





class A(threading.Thread):
    def __init__(self,url,q):
        super().__init__()
        self.url = url
        self.q = q

    def run(self):
        a = etree.HTML(requests.get(self.url).content.decode('utf-8'))
        li = a.xpath("//div[@class='dictorsmx studio']/dl/dd[@class='name']/a/@href")

        for i in li:
            list1 = []
            l = 'http://www.hnzhy.com/'+i
            n_l = etree.HTML(requests.get(l).content.decode('utf-8'))

            name = n_l.xpath("//dd[@id='DDName']/text()")[0]
            duty = n_l.xpath("//dd[@id='DDPosition']/text()")[0]
            expert = n_l.xpath("//div[@id='DIVContent']//text()")

            list1.append(name)
            list1.append(duty)
            list1.append("".join(expert))

            self.q.put(list1)
        print("存入完成")



class B(threading.Thread):
    def __init__(self,q):
        super().__init__()
        self.q=q

    def run(self):
        conn = sqlite3.connect("1903c.db")
        cur = conn.cursor()

        print("开始建表")
        try:
            cur.execute("CREATE TABLE old_doctor(id INTEGER PRIMARY KEY  AUTOINCREMENT,"
                                                "name CHAR(6),"
                                                "duty TEXT,"
                                                "expert TEXT)")
        except Exception:
            print("表已存在")

        finally:
            while True:
                try:
                    one_p = self.q.get(timeout=6)
                    cur.execute("INSERT INTO old_doctor(name,duty,expert) "
                                "VALUES (?,?,?)",(one_p[0],one_p[1],one_p[2]))
                    print(one_p[0]+"存入成功")

                except:
                    conn.commit()
                    print("全部存入成功")

                    break
        conn.close()



if __name__ == '__main__':
    q = queue.Queue()
    url = 'http://www.hnzhy.com/TDoctors.html'

    A = A(url,q)
    B = B(q)
    B.start()
    A.start()







