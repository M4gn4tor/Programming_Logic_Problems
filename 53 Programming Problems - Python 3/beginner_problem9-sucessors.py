# Write a program that asks for integers I (-4000<=I<=4000)
# while I is different than zero. When I is equals to zero,
# the program must print all imediate integer sucessors of
# each I inserted.

# Note that in this problem, there is no limit for the quantity
# of I numbers informed.

n = 8000
_list = []
while not -4001 <= int(n) <= 4001:
    n = int(input("Digite um numero: "))
    if n != 0:
        n += 1
        _list.append(str(n))
    else:
        break

var = "\n".join(_list)

print(var)

# Test

# Input:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 0
# Expected output:
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
