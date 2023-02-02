import time
import random

def fib(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

y = 15 + (35-15) * random.random()
start = time.time()
total = fib(int(y))
end = time.time()

print("fib ({}) = {}".format(int(y), total))
print("took: {:.9f} seconds".format(end-start))
