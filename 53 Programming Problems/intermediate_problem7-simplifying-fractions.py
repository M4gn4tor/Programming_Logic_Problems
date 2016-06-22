# Considere a fraction in the format N/M where N is an integer (0<=N<=10000) and
# M is an integer (1<=M<=10000).
# Write a program that's capable of simplifying a fraction in this format such
# as the new numerator and the new denominator are primes to one another.
# The program will receive a bunch of tests, in an indefined number of lines.
# Each line will have the integer N and M separeted by a blank space. The end
# of the input will be when N=M=0.
# The output must be a simplified fraction in the same order as the input, each
# one in a line displaying N and M

numerator = 1
denominator = 1
numeratorList = []
denominatorList = []
while 0 <= int(numerator) <= 10000 and 1 <= int(denominator) <= 10000:
    _input = raw_input()
    numerator, denominator = _input.split(" ")
    if 0 <= int(numerator) <= 10000 and 1 <= int(denominator) <= 10000:
        numeratorList.append(int(numerator))
        denominatorList.append(int(denominator))

print "Output:"

maxDivisor = 1

for i in range(len(numeratorList)):
    for j in range(2, numeratorList[i]):
        if numeratorList[i] % j == 0:
            if j > maxDivisor:
                maxDivisor = j
    for j in range(2, denominatorList[i]):
        if denominatorList[i] % j == 0:
            if j > maxDivisor:
                maxDivisor = j
    outputNumerator = numeratorList[i] / maxDivisor
    outputDenominator = denominatorList[i] / maxDivisor
    print "%d %d" % (outputNumerator, outputDenominator)
    maxDivisor = 1

# Test
# Input:
# 0 1
# 1 1
# 2 2
# 2 4
# 9 3
# 25 625
# 0 0
# Expected output:
# 0 1
# 1 1
# 1 1
# 1 2
# 3 1
# 1 25
