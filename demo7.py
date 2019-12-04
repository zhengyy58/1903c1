import queue


q = queue.Queue(10)

# print(q.qsize())

# for i in range(1,12):
#     print(q.full())
#     try:
#         q.put(i,timeout=5)
#         print("{}存入".format(i))
#     except Exception:
#         print("队列已满，无法再次存入")



# print(q.qsize())

q.empty()
print(1)
print(q.get(timeout=5))
print(2)
# print(q.get())
# print(q.get())
# print(q.get())

# print(q.qsize())

