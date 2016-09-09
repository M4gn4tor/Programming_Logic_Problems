# A word W with length L (2<=L<=100) is magic if it has an even number of
# characters and if when sorting the first L/2 characters in alphabetic order we
# obtain the latter L/2 characters:

# Examples of magic words:
# asas
# gogo
# gluglu
# chocho
# asdfasdf
# aaaa

# Examples of words that are not magic:
# xixi (when sorting the first half we have 'ix' that's different from 'xi')
# xoxo (when sorting the first half we have 'ox' that's different from 'xo')
# asdfddsa (first half sorted ('asdf') and latter half ('fdsa') are different)
# aaaaa (it is not magic, because it has an odd length)

# Write a program that, having a word as input is capable of identifying whether
# the word is magic or isn't. If it is, display 'Y', if it isn't, display 'N'.

word = ''
while not 2 <= len(word) <= 100:
    word = raw_input("Type a magic word: ")

if len(word) % 2 == 0:
    first_half = ''
    second_half = ''
    for i, j in zip(range(len(word)/2), range(len(word)/2, len(word))):
        first_half = first_half + word[i]
        second_half = second_half + word[j]
    if ''.join(sorted(first_half)) == second_half:
        print 'Y'
    else:
        print 'N'
else:
    print 'N'

# Test
# Input:
# popo
# Expected output:
# N

# Input:
# gugu
# Expected output:
# S

# Input:
# tutu
# Expected output:
# S

# Input:
# aaaaa
# Expected output:
# N

# Input:
# tatatt
# Expected output:
# S
