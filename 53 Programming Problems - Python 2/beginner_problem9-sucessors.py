# Write a program that asks for integers I (-4000<=I<=4000)
# while I is different than zero. When I is equals to zero,
# the program must print all imediate integer sucessors of
# each I inserted.

# Note that in this problem, there is no limit for the quantity
# of I numbers informed.

n = 1
_list = []
while -4001 <= n <= 4001:
    n = input("Digite um numero: ")
    if n != 0:
        n += 1
        _list.append(str(n))
    else:
        break

print "\n".join(_list)

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