#  1st

# import threading
# def worker():
#     print("hello from worker thread ")
# t1=threading.Thread(target=worker)
# t1.start()
# print("hello from main thread")
# t1.join()
# print("main thread completed")

# 2nd
# import threading
# def fun(name):
#     for i in range(1, 6):
#         print(name, ":", i)
# t1 = threading.Thread(target=fun, args=("Thread-1",))
# t2 = threading.Thread(target=fun, args=("Thread-2",))
# t3 = threading.Thread(target=fun, args=("Thread-3",))
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()

# 3rd
# import threading
# def fun(a, b):
#     c = a + b
#     print("Sum:", c)
# t1 = threading.Thread(target=fun, args=(10, 20))
# t1.start()
# t1.join()
# print("Main completed")

# 5th
# import threading
# counter = 0
# lock = threading.Lock()
# def fun():
#     global counter
#     for i in range(100000):
#         with lock:
#             counter += 1
# t1 = threading.Thread(target=fun)
# t2 = threading.Thread(target=fun)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Final counter:", counter)

# 6th
# import threading
# import time
# def fun1():
#     print("A started")
#     time.sleep(2)
#     print("A completed")
# def fun2():
#     print("B started")
# t1 = threading.Thread(target=fun1)
# t2 = threading.Thread(target=fun2)
# t1.start()
# t1.join()
# t2.start()
# t2.join()
# print("Main completed")


# import threading
# def worker():
#     print("hello from worker thread")
# t1=threading.Thread(target=worker)
# t1.start()
# print("hello from main thread")
# t1.join()
# print("main thread completed")

# import threading
# def fun(name):
#     for i in range(1,5):
#         print(name,"->",i)
# t1=threading.Thread(target=fun,args=("Thread-1",))
# t2=threading.Thread(target=fun,args=("Thread-2",))
# t3=threading.Thread(target=fun,args=("Thread-3",))
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()

# import threading
# def fun(a,b):
#     c=a+b
#     print("sum:",c)
# t1=threading.Thread(target=fun,args=(20,14))
# t1.start()
# t1.join()
# print("main completed")

# import threading
# import time
# def fun():
#     print("a started")
#     time.sleep(2)
#     print("a completed")
# def fun2():
#     print("b started")
# t1=threading.Thread(target=fun)
# t2=threading.Thread(target=fun2)
# t1.start()
# t1.join()
# t2.start()
# t2.join()
# print("main completed")