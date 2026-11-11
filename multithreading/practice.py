# import threading
# def fun(x,name):
#     for i in range(x):
#         print(i)
#     print(f"{name} completed")
# t1=threading.Thread(target=fun,args=(3,"the"))
# t2=threading.Thread(target=fun,args=(4,"there"))
# t1.start()
#
# t1.join()
#
# t2.start()
#
# t2.join()
# print("main thread completed")

# import threading
# def display():
#     print("helloworld")
# t1=threading.Thread(target=display)
# t1.start()
# t1.join()
# print("main thread")

# import threading
# def numbers():
#     for i in range(1,10):
#         print(i)
# t1=threading.Thread(target=numbers)
# t1.start()

# import threading
# def numbers():
#     for i in range(1,20):
#         if i%2==0:
#             print(i)
# t1=threading.Thread(target=numbers)
# t1.start()

# import threading
# import time
# def task(x):
#     for i in range(x):
#         print(f"{threading.current_thread().name}: {i}")
#         time.sleep(1)
# t1 = threading.Thread(target=task, args=(5,), name="Thread-1",daemon=True)
# def task2():
#     print(f"{threading.current_thread().name}: Started")
#     t1.join()
#     print(f"{threading.current_thread().name}: completed")
#
# t2 = threading.Thread(target=task2, name="Thread-2",daemon=True)
# t1.start(); t2.start()
# print("Main Thread Completed")
# t2.join()
# t1.run();t2.run()
# print("Main Thread Completed")
# print(t1.is_alive())
# print(t2.is_alive())

# import threading
# def fun(x,name):
#     for i in range(x):
#         print(i)
#     print(f"{name} completed")
# t1=threading.Thread(target=fun,args=(3,"the"))
# t2=threading.Thread(target=fun,args=(4,"there"))
# t1.run();t2.run()
# print("main thread completed")

# import threading
# balance = 1000
# def withdraw(amount):
#     global balance
#     balance = balance - amount
#     print("Balance:", balance)
# t1 = threading.Thread(target=withdraw, args=(500,))
# t2 = threading.Thread(target=withdraw, args=(300,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Final balance:", balance)

import threading
def worker():
    print("hello from worker thread ")
t1=threading.Thread(target=worker)
t1.start()
print("hello from main thread")
t1.join()
print("main thread completed")


