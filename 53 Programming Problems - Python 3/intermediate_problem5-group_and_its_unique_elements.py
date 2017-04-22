# By definition, a group can't have repeated numbers.
# Write a program, that's able to read a number N (1<=N<=1000) and N integers K
# (-1000<=K<=1000).
# The output must be a group formed by the K integers. The numbers have to be
# displayed in ascending order.

# Read number N
n = 0
while not 1 <= int(n) <= 1000:
    n = int(input("Type an integer from 1 to 1000: "))

integers = []
k = 0
# Write integers to list
for _ in range(n):
    k = int(input("Type an integer: "))
    if -1000 <= k <= 1000:
        integers.append(k)
    else:
        _ -= 1

# Convert list to set (unique values) and sort it
print("{a}".format(a=sorted(set(integers))))
