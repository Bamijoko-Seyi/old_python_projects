from time import process_time

# we want to calculate some number base to
# the power of pow mod some number divisor
# we want to compute base^power % divisor

base = 7
power = 66000000 # n
divisor = 2

# fastest (for some really big problem)
# constant time: O(1)
# logarithmic time: O(log(n))
# linear time: O(n)
# log-lin time: O(n*log(n))
# quadratic time: O(n^2)
# cubic time: O(n^3)
# exponential time: O(2^n)
# slowest

def example(n):
    for i in range(n):
        for j in range(n):
            pass # something????

def compute_1(base, power, divisor):
    return base ** power % divisor

#(a*b)%c = (a%c)*(b%c)


def compute_2(base, power, divisor): # O(n^3)
    product = 1
    for _ in range(power): # this loop makes it bigger than n^2
        product = product * base # O(n^2) (n is the number of digits)
    return product % divisor

# (x^3)*(x^3) = (x^6)

def compute_2b(base, power, divisor): # O(log(n))
    product = 1
    # we can replace this loop with a trick!!!!
    #for _ in range(power): # this loop makes it bigger than n^2
    #    product = product * base % divisor # O(1) (n is the number of digits)
    return product % divisor


def compute_3(base, power, divisor):
    return pow(base, power) % divisor

def compute_4(base, power, divisor):
    return pow(base, power, divisor)

def time_it(base, power, divisor, function):
    start = process_time()
    result = function(base, power, divisor)
    end = process_time()
    print(end - start, "seconds")
    return result

print(time_it(base, power, divisor, compute_1))
print(time_it(base, power//10, divisor, compute_2))
print(time_it(base, power, divisor, compute_3))
print(time_it(base, power, divisor, compute_4))

def compute_5(base, power, divisor):
    pow(base, power) % divisor
    return pow(base, power) % divisor

def compute_6(base, power, divisor):
    for _ in range(10000000):
        a = 10
    return pow(base, power) % divisor


print(time_it(base, power, divisor, compute_5))
print(time_it(base, power, divisor, compute_6))




# big-O notation

# if one algorithm always takes twice as long as
# another, we don't care!

# we want to consider them the same time complexity

# if one algorithm always takes + 1 second compared
# to another aglorithm,
# we want to consider them the same time complexity





