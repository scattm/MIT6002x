import numpy

s = {
    "A": [0, 1, 2, 3, 4, 5, 6, 7, 8],
    "B": [5, 10, 10, 10, 15],
    "C": [0, 1, 2, 4, 6, 8],
    "D": [6, 7, 11, 12, 13, 15],
    "E": [9, 0, 0, 3, 3, 3, 6, 6]
}

for l in s.keys():
    print "%s:" % l,
    print numpy.average(s[l]),
    print numpy.var(s[l])


def possible_mean(L):
    return sum(L) / len(L)


def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e - mu) ** 2
    return temp / len(L)


for l in s.keys():
    print "%s:" % l,
    print possible_variance(s[l])
