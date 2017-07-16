#!/bin/python

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    # your code goes here
    n = len(s)
    length = 1
    found = False
    while length * 2 <= n:
        i = length
        start = int(s[0:length])
        prev = start
        t_len = length
        while i + t_len <= n:
            nex = prev + 1
            t_len = len(str(nex))
            nex_str = int(s[i:i + t_len])
            if nex_str != nex or s[i] == '0':
                break
            if nex_str == nex and i + t_len == n:
                found = True
            prev = nex_str
            i += t_len
        length += 1
        if found:
            print 'YES', start
            break
    if not found:
        print 'NO'
