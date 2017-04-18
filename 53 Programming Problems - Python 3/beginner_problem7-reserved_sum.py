# For this problem, consider that the reserved sum of N + M is
# given by Rev(Rev(N) + Rev(M)), with Rev(X) being the function
# that returns the number with its algarisms reversed,
# e.g. Rev(5789) = 9875

# Write a program that receives two integers and returns its
# reserved sum

iN = int(input("Type N\n"))
iM = int(input("Type M\n"))

sN = str(iN)
sM = str(iM)

sRevN = [0] * len(sN)
sRevM = [0] * len(sM)

count = len(sN) - 1

for i in range(len(sN)):
    sRevN[i] = sN[count]
    count -= 1

count = len(sM) - 1

for j in range(len(sM)):
    sRevM[j] = sM[count]
    count -= 1

iRevN = int("".join(sRevN))
iRevM = int("".join(sRevM))

iTotal = iRevN + iRevM

sTotal = str(iTotal)

count = len(sTotal) - 1

sResult = [0] * len(sTotal)

for i in range(len(sTotal)):
    sResult[i] = sTotal[count]
    count -= 1

print(("Result: %d\n") % int("".join(sResult)))

# Test

# Input:
# 1000
# 1200
# Expected output:
# 22

# Input:
# 5
# 130000
# Expected output:
# 63
