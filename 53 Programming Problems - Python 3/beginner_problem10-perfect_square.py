# A positive integer N is a perfect square if there
# is a number K where K*K=N

# Write a program that receives an indefined quantity
# of positive integers J (-10000<=J<=10000) until J is
# equals to zero. The output must be quantity of perfect
# squares input.

n = 0
_sum = 0
while -1000 <= int(n) <= 1000:
    n = int(input("Type a positive integer number: "))
    if n != 0:
        for i in range(0, n / 2 + 1):
            if pow(i, 2) == n:
                _sum += 1
        if n == 1:
            _sum += 1
    else:
        break

print(_sum)

# Test

# Input:
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 0
# Expected output:
# 2

# Input:
# 4
# 9
# 16
# 144
# 0
# Expected output:
# 4
