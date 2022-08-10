from threading import*

import time 

def f1():
    for x in range(5):
        time.sleep(4)

        print(x)


def f2():
    for x in range(6,10):
        time.sleep(2)
        
        print(x)
    print("id",)

t1=Thread(target=f1,name="thread1")
t1.start()
t2=Thread(target=f2,name="thread2")
t2.start()
