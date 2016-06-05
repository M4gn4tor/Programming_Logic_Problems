# Write a program that:
# - Reads a number N
# - Read N sequencies of 5 integers each
# - Print the N sequencies, alternating the order
# between ascending and descending

# Variation 1
# Solve the same problem, but assume that the number of elements in each
# sequence can vary. Before inputing each sequence, the user informs the number
# of elements in the sequence.

# Variation 2
# Write the same program, but when printing:
# - Ascending order: when there's no prime number
# - Descending order: when there's one prime number
# - Same order as input: when there's more than one prime number

n = 0
while not 0 < n <= 1000:
    n = input("Type the number of sequences: ")

_list = []
size = []

for i in range(n):
    size.append(input("Type the number of elements in the sequence: "))
    for _ in range(size[i]):
        _list.append(input())

aux_list = []
index_element_list = 0

for i in range(len(size)):
    for j in range(size[i]):
        aux_list.append(_list[index_element_list])
        index_element_list += 1
        if j == size[i] - 1:
            prime_count = 0
            for num in aux_list:
                count = 0
                for i in range(2, num):
                    if (float(num) / i % 1) == 0:
                        count = 1
                        break
                if count == 0:
                    prime_count += 1
            if prime_count == 0:
                print sorted(aux_list)
            elif prime_count == 1:
                print sorted(aux_list, reverse=True)
            else:
                print aux_list
            aux_list = []

# Test
