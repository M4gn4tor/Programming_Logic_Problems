# Goldbach conjecture (still not proved) says that any even number
# equal or greater than 4 is the sum of two prime numbers.

# Write a program that, by receiving an even number N (2<=N<=4294967294)
# is able to return two integers that are the two prime numbers that the
# sum is equal to N

# Considere that:
# - The returned numbers must be in ascening order.
# - If there is more than one option, returns the one that the first
# number is lesser
# - Not existing results (Congrats, you're the first one in the world to
# prove the conjucture to be false), return -1

# Remember: prime number is that one that can only be divided by 1 and itself

n = 0
while not 2 <= n <= 4294967294:
    n = int(input("Type a number between 2 and 4294967294: "))

prime = []
prime.append(2)
prime.append(3)
control = False
for i in range(3, n+1):
    for j in range(2, i):
        if i % j == 0:
            control = True
    if not control:
        prime.append(i)
    control = False

stop = False
for i in range(len(prime)):
    for j in range(i, len(prime)):
        if prime[i] + prime[j] == n:
            print("%d + %d" % (prime[i], prime[j]))
            stop = True
    if stop:
        break

# Test

# Input:
# 720
# Expected output:
# 11
# 709

# Input:
# 666
# Expected output:
# 5
# 661
