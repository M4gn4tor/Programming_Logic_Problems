# Fibonaacci is a sequence built in a way that each term is
# the sum of the two last terms. For example: 0, 1, 1, 2, 3, 5,
# 8, 13.
#
# Write a program that's able to ask an integer N (1 <= N <= 40)
# and return the first N terms (one term per line) of the Fibonacci
# sequence with 0 as the first term and 1 as the second one

n1 = 0
n2 = 1
N = 0
while not 1 <= N <= 40:
    N = int(input("Type how many terms you want to see: "))
print("%d\n%d" % (n1, n2))
for _ in range(2, N):
    aux = n2 + n1
    n1 = n2
    n2 = aux
    print ("%d" % n2)

# Test

# Input:
# 20
# Expected output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
# 233
# 377
# 610
# 987
# 1597
# 2584
# 4181

# Input:
# 1
# Expected output:
# 0
