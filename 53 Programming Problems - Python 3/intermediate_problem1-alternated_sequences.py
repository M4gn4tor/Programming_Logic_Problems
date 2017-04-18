# Write a program that:
# - Reads a number N
# - Read N sequencies of 5 integers each
# - Print the N sequencies, alternating the order
# between ascending and descending

n = 0
while not 0 < int(n) <= 1000:
    n = int(input("Type the number of sequences: "))

_list = []

for _ in range(n):
    for _ in range(5):
        _list.append(input())

aux_list = [0] * 5
j = 0
while j < len(_list):
    for i in range(5):
        aux_list[i] = _list[j]
        j += 1
    if j % 2 != 0:
        print("{a}".format(a=sorted(aux_list)))
    else:
        print("{a".format(a=sorted(aux_list, reverse=True)))

# Test

# Input:
# 4
# 87
# 55
# 34
# 0
# 53
# 21
# 8
# 61
# 82
# 9
# 80
# 78
# 1
# 10
# 99
# 4
# 78
# 43
# 71
# 23
# Expected output:
# 0 34 53 55 87
# 82 61 21 9 8
# 1 10 78 80
# 78 71 43 23 4
