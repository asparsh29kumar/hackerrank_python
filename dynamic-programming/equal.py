# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(raw_input())):
    n = int(raw_input())
    choco_list = map(int, raw_input().split(' '))
    ma = max(choco_list)
    mi = min(choco_list)
    sub = [0, 1, 2, 5]
    count = [0 for _ in range(4)]
    for j in range(4):
        for i in range(n):
            temp = choco_list[i]
            temp -= (mi - sub[j])
            count[j] += int(temp / 5)
            temp %= 5
            count[j] += int(temp / 2)
            temp %= 2
            count[j] += temp
    print min(count)
