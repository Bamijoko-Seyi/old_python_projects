from random import randrange
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
       total_time += time_one(f, n)
    print("Average time: ", total_time/RUNS)

# Search... finding something in a big list of things...

def make_list(size):
    new_list = []
    for i in range(size):
        new_list.append(randrange(size*size))
    return new_list

def maximum(l): # O(n)
    max_so_far = 0 # we have to pick the starting number so its less than every possible number
    for number in l:
        if number > max_so_far:
            max_so_far = number
    return max_so_far

def maximum_sorted(l):
    l = sorted(l) # sorting is typically O(n*log(n))
    return l[-1]

def find(l, target):
    for index in range(len(l)):
        if l[index] == target:
            return index

def test_find(l):
    random_index = randrange(len(l))
    target = l[random_index]
    assert find(l, target) == random_index

l = make_list(10000000)
assert maximum(l) == max(l)
assert maximum_sorted(l) == max(l)
#time_many(maximum, l)
#time_many(maximum_sorted, l)
#time_many(test_find, l)

# constant time - but we can only use it if the list is already sorted!
def maximum_already_sorted(l):
    return l[-1]

l = sorted(l)
assert maximum_already_sorted(l) == max(l)
time_many(maximum_already_sorted, l)

# BINARY SEARCH - we can only use it if the list is already sorted!
def find_already_sorted(l, target):
    lower_index = 0
    upper_index = len(l)
    iterations = 0
    while lower_index < upper_index:
        iterations += 1
        middle_index = (lower_index + upper_index) // 2
        middle_value = l[middle_index]
        if target == middle_value:
            print(iterations)
            return middle_index
        elif target < middle_value:
            upper_index = middle_index
        else: # target > middle_value
            lower_index = middle_index
    print(iterations)
    return lower_index
        

def test_find_already_sorted(l):
    random_index = randrange(len(l))
    target = l[random_index]
    found_index = find_already_sorted(l, target)
    #print(found_index, random_index)
    assert found_index == random_index

time_many(test_find_already_sorted, l)
# for 100,000: 14-17 iterations
# for 1,000,000: 13-20 iterations
# for 10,000,000: 18-24 iterations
# we can predict, for 100,000,000: max 28 iterations
# we can predict, for 1,000,000,000: max 32 iterations

# number of steps the computer needs to do ~ number of iterations
# number of iterations is ~ log(input size)

# if something takes 4n steps for an input n, we call that O(n)
# if something takes 5n steps for an input size n, we call that O(n)
# log_b(n) = log(n)/log(b)





