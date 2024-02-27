def my_min(list_of_numbers):
    cur_min = list_of_numbers[0]
    for number in list_of_numbers[1:]:
        if number < cur_min:
            cur_min = number
    return cur_min


def sum_first_n_whole_numbers_v1(n):
    # T(n) = n*2
    # we can multiply this one by 3/2 to get the same speed as v1_alt
    # T(n) is in O(n)

    total = 0
    for number in range(n+1):
        total+=number
    return total

def sum_first_n_whole_numbers_v1_alt(n):
    # T(n)= n*3
    # T(n) is in O(n)
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
    # T(n) = 3
    # T(n) is in O(1)
    return (n * (n + 1)) // 2

def sum_first_n_whole_numbers_v4(n):
    # T(n) = 10000003
    # T(n) is in O(1)
    j = 0
    for i in range(10000000):
        j = i
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
    average = total_time/RUNS
    print(average)
    return average
    
import matplotlib.pyplot as plt

def benchmark():
    ns = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000]
    v1_times = []
    v1_alt_times = []
    v3_times = []
    v4_times = []
    for n in ns:
        v1_times.append(time_many(sum_first_n_whole_numbers_v1, n))
        v1_alt_times.append(time_many(sum_first_n_whole_numbers_v1_alt, n))
        v3_times.append(time_many(sum_first_n_whole_numbers_v3, n))
        v4_times.append(time_many(sum_first_n_whole_numbers_v4, n))
    plt.plot(ns, v1_times)
    plt.plot(ns, v1_alt_times)
    plt.plot(ns, v3_times)
    plt.plot(ns, v4_times)
    plt.show()

def main():
    benchmark()

if __name__=='__main__':
    main()




