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

# Variation 3
# Solve the same problem, alternating the ascending and descending orders, but
# do it according to the weight W defined below:
# - The weight W of each element is the quantity of positive integers divisors
# that it has.

n = 0
while not 0 < n <= 1000:
    n = input("Type the number of sequences: ")

_list = []
aux_list = []
aux_list2 = []
index_element_list = 0
int_div = 0

for i in range(n):
    for j in range(5):
        _list.append(input())
        int_div = 0
        item = _list[index_element_list]
        index_element_list += 1
        for num in range(2, item):
            if item % num == 0:
                int_div += 1
        aux_list.append(int_div)
    for j in range(5):
        max_value = max(_list)
        _item = _list.index(max_value)
        aux_list2.append(_item)
        _list.remove(_item)
    if i % 2 == 0:
        print sorted(aux_list2)
    else:
        print sorted(aux_list2, reverse=True)

    _list = []
    _aux_list2 = []

# Test
