with open("frank.txt") as frankenfile:
    lines = frankenfile.read().splitlines()

line_words = []
for line in lines:
    line_words.append(len(line.split()))

line_words = [len(line.split()) for line in lines]

print(line_words[:100])

franks = []
for line in lines:
    if "FRANKENSTEIN" in line:
        franks.append(line)

# ranks = [line for line in lines] # copies lines
franks = [line for line in lines
            if "FRANKENSTEIN" in line]

# the general format is
# [expression you would have appened
#  the for loop (without the :)
#  optional if]

# to use filter we need a function that returns
# True/False
def has_frank(line):
    return "FRANKENSTEIN" in line

franks = list(filter(has_frank, lines))

# make my own generator
franks = (line for line in lines
            if "FRANKENSTEIN" in line)

print(franks)

# Please take the USRI/SPOT
# https://p20.courseval.net/etw/ets/et.asp?nxappid=UA2&nxmid=start

