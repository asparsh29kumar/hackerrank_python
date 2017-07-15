# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(raw_input())):
    n = int(raw_input())
    arr = map(int, raw_input().split(' '))
    take = 0
    notake = 0
    for i in range(1, n):
        a1 = notake + abs(1 - 1)
        b1 = take + abs(1 - arr[i - 1])
        a = notake + abs(1 - arr[i])
        b = take + abs(arr[i] - arr[i - 1])
        notake = max(a1, b1)
        take = max(a, b)
    print max(take, notake)
