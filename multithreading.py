import threading
import math
import random

event = threading.Event()
def num_of_batches(batches_number):
    c = 0  # inside the circle
    n = 0  # all points
    for i in batches_number:
        for j in range(1000000):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            n += 1
            if x**2+y**2 < 1:
                c += 1

        print("the real pi is " + str(math.pi))
        print("the calculated pi is " + str(c/n*4))
        print("the numbers of trys is " + str(n))
        if event.is_set():
            break

batches_number = input("enter your number: ")
t1 = threading.Thread(target=num_of_batches, args=batches_number, )
t1.start()
t1.join()






