import threading
from threading import Lock

class a(threading.Thread):
    def __init__(self,name):
        super().__init__()
        # threading.Thread.__init__(self)
        self.name = name

    def run(self):
        # lock.acquire()
        print("我是{}".format(self.name))
        # lock.release()



if __name__ == "__main__":

    lock = Lock()

    A = a("小王")
    B = a("老王")
    A.start()
    B.start()







