def my_min(list_of_numbers):
    cur_min = list_of_numbers[0]
    for number in list_of_numbers[1:]:
        if number < cur_min:
            cur_min = number
    return cur_min


def sum_first_n_whole_numbers_v1(n):
    total = 0
    for number in range(n+1):
        total+=number
    return total

def sum_first_n_whole_numbers_v1_alt(n):
    total = 0
    number = 1
    while number <= n:
        total+=number
        number+=1
    return total

def sum_first_n_whole_numbers_v2(n):
    if n == 1:
        return 1
    return sum_first_n_whole_numbers_v2(n-1)+n

# in some programming languages v1 and v2 are the same algorithm
# but in Python they are not the same algorithm

def sum_first_n_whole_numbers_v3(n):
    return (n * (n + 1)) // 2

import time

def time_one(f, n):
    start=time.time()
    f(n)
    end=time.time()
    return end-start

def time_many(f, n):
    RUNS=10
    total_time=0
    print(f, n)
    for sample in range(RUNS):
       total_time += time_one(f, n)
    print(total_time/RUNS)

#sum_first_n_whole_numbers_v1(100000000)


time_many(sum_first_n_whole_numbers_v1, 10000000)
time_many(sum_first_n_whole_numbers_v1_alt, 10000000)
#time_many(sum_first_n_whole_numbers_v2, 10000000)
time_many(sum_first_n_whole_numbers_v3, 10000000)




