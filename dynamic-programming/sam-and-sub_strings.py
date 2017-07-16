number = raw_input()
mod_number = 10 ** 9 + 7
total = 0
length = len(number)
multiplier = 1
for i in range(length - 1, -1, -1):
    temp = (multiplier * int(number[i]) * (i + 1)) % mod_number
    total += temp
    total %= mod_number
    multiplier = (multiplier * 10 + 1) % mod_number
print total
