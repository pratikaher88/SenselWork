from multiprocessing import Process
import random
import time

def some_function(first, last):
    print("FIRST LAST",first,last)
    # time.sleep(random.randint(1, 3))
    # print(first, last)

processes = []

for m in range(1,16):
   n = m + 1
   print("M N",m,n)
   p = Process(target=some_function(m,n))
   p.start()
