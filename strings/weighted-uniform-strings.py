#!/bin/python


def add_dictionary(dictionary, num):
    key = num % 27
    dictionary[key - 1].append(num)


def is_present(dictionary, num):
    key = num % 27
    return num in dictionary[key - 1]


s = raw_input().strip()
length = len(s)
i = 0
dic = [[] for _ in range(26)]
while i < length:
    start = ord(s[i]) - ord('a') + 1
    add_dictionary(dic, start)
    total = start
    i += 1
    while i < length and (ord(s[i]) - ord('a') + 1) == start:
        total += start
        i += 1
        add_dictionary(dic, total)

n = int(raw_input().strip())
for a0 in xrange(n):
    x = int(raw_input().strip())
    # your code goes here
    if is_present(dic, x):
        print 'Yes'
    else:
        print 'No'
