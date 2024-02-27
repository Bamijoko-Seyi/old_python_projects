from random import randrange
from random import shuffle
import time

def time_one(f, n):
    start=time.time()
    f(n)
    end=time.time()
    return end-start

def time_many(f, n):
    RUNS=10
    total_time=0
    print("start:", f.__name__)
    for sample in range(RUNS):
        shuffle(n)
        total_time += time_one(f, n)
    average = total_time/RUNS
    return average

def make_list(size):
    assert size < 100000000 # fills up my computer lol
    print("Getting numbers...")
    new_list = list(range(size))
    print("Shuffling...")
    shuffle(new_list)
    print("Done.")
    return new_list
    while len(new_list) < size:
        new_list.extend([randrange(size*size) for _ in range((size - 1) % 1000000 + 1)])
        print(len(new_list))
    return new_list

# O(n^2)
def insertion_sort(a_list):
    new_list = list()
    for item in a_list:
        inserted = False
        for index in range(len(new_list)):
            if item < new_list[index]:
                new_list.insert(index, item)
                inserted = True
                break
        if not inserted:
            new_list.append(item)
    return new_list

"""
x
x
xx
xxx
xxxx
xxxxx
xxxxxx
xxxxxxx
xxxxxxxx
xxxxxxxxx

"""

print(make_list(10))

for size in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
    a_list = make_list(size)
    t = time_many(sorted, a_list)
    print(f"Size: {size} time: {t}")

# for python's sorted O(n*log(n))







