# Sillable's separator (light version)

# Generally, text processors use some kind of algorithm to put hifens in words.
# In this algorithm are they are considered positions, where the word can be
# split. For example, the word "programacao" can be split into "pro-gramacao",
# "progra-macao" and "programa-cao".
#
# Write a program that, receiving a characters chain (50 chars max) on the
# format below, display all possible syllable divisions possible (one per line),
# in order of preference of the word represented.
#
# Input format and general instructions:
# <letter0><digit0><letter1><digit1>...<lettern><digitn>
#
# Where:
#   - <lettern> is a lowercase letter of the alphabet
#   - <digitn> can be omitted and it is a posivite integer from 1 to 9
# If <digit0> is an even number, the place can't be split, otherwise it can.
# Greater numbers show where it is preferable to split the word.
# If there are more than a spot with the same preference, all options must be
# displayed. The separations must be shown where the hifen is closer to the left
# side.

raw_message = raw_input("Type the word: ")

letter_digit = []
aux_sillable = str()
i = 0
for i in xrange(len(raw_message)):
    if raw_message[i].isalpha():
        aux_sillable += raw_message[i]
        i += 1
    elif raw_message[i].isdigit():
        letter_digit.append([aux_sillable, raw_message[i]])
        i += 1
        aux_sillable = ""
if len(aux_sillable) > 0:
    letter_digit.append([aux_sillable, 0])

print letter_digit
