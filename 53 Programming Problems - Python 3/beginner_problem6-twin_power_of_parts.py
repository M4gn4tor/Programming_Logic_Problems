# There are some numbers that have a very interesting property:
# 100       10+0=10         10*10=100
# 2025      20+25=45        45*45=2025
# 3025      30+25=55        55*55=3025
# 9801      98+01=99        99*99=9801
# 10000     100+0=100       100*100=1000
# 88209     88+209=297      297*297=88209
# 494209    494+209=703     703*703=494209
# 998001    998+1=999       999*999=998001

# Numbers that have this property are known as Kaprekaer numbers.
# Each of the numbers shown, had its numbers decomposed in a way that
# the sum of the parts powered of 2 is equal to the original number.

# Write a program that's able to read and identify if a number N
# (1<=N<=100,000,000) has or hasn't this property. If so, the program
# returns 1, otherwise it returns 0.

n = 0
while not 1 <= n <= 100000000:
    n = int(input("Type a number between 1 and 100,000,000 (no commas)\n"))

part1 = int(str(n)[:len(str(n))//2])
part2 = int(str(n)[len(str(n))//2:])

# Test for even numbers and odd numbers (e.g. 12345, test for 12 + 345)
if pow(part1 + part2, 2) == n:
    print("1")
# if the number is odd, tests for another possibility
# (e.g. 12345, test for 123 + 45)
else:
    if len(str(n)) % 2 != 0:
        odd_part1 = int(str(n)[:len(str(n))//2+1])
        odd_part2 = int(str(n)[len(str(n))//2+1:])
        if pow(part1 + part2, 2) == n:
            print("1")
        else:
            print("0")
    else:
        print("0")

# Test

# Input:
# 60481729
# Expected output:
# 1

# Input:
# 60481728
# Expected output:
# 0

# Input:
# 300814336
# Expected output:
# 1

# Input:
# 88200
# Expected output:
# 0
