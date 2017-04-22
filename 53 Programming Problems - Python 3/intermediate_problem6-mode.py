# Mode is the group of most frequent numbers in a sample. For example, in the
# sample (1,2,3,3,3,4,4,4,4,5) the mode is {4}, in the sample
# (1,1,1,2,2,2,3,4,5,5,6) the mode is {1, 2}
# Write a program that's able to calculate the mode of a sample of K numbers.
# The input will be an undefined quantity of K elements, one per line.
# The output will be the mode elements of K, in ascending order, one per line.
# K will have as elements integers between 0 and 256, as 0 means end of input.

integers = []
n = 1
print("Type integers between 0 and 256, one per line")
while int(n) != 0:
    n = int(input())
    if 0 < n < 256:
        integers.append(n)

max_count = max((integers.count(x)) for x in set(integers))
print("Mode(s):")
for x in sorted(set(integers)):
    if integers.count(x) == max_count:
        print(x)
