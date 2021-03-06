# Create a program that's capable of identifying an enemy message that's being
# transmitted via radio waves over 100MHz. The spy software Kni has already
# captured the transmission and it is necessary to create another software
# that's capable of interpreting and extracting the message.

# Kni gives an output as follows:
# 90c87esd67uj,./';*&^120lin87uj101gu87km102a77jh150gem..&

# Where, from left to right:
# 90 is the frequency in MHz
# c is the code read in the 90MHz frequency
# 87 is the frequency of the next code
# esd is the code read in the 87 frequency
# 67 is the frequency of the next code
# uj is the code read in the 67 frequency
# ,./';&^ was an interferency that occurred when 67 was being read
# ...

# So, from the chunk above, the message read above 120MHz was: "linguagem".
# Because "lin" was transmitted on the 120MHz frequency, "gu" was transmitted on
# the 101MHz frequency, "a" on the 102 one and "gem" on the 150MHz one.

# Write a program that, receiving a 250 characters message, is able to retrive
# the message transmitted over 100MHz.

# Consider that:
# - The frequency is always from 1 to 200
# - Every interferency must be ignored. Must be considered as an interferency
# every character that's neither a letter nor a number.
# - There will be no blank spaces in the string generated by Kni
# - The message's max length is 100 characteres

string = str()
while len(string) < 1 or len(string) > 250:
    string = input("Type the message captured by Kni: ")

message = str()
message_without_interference = str()
# Remove all interferences from string
for i in range(len(string)):
    if string[i].isalnum():
        message_without_interference += string[i]

message = str()
frequency = str()
final_message = str()
index = 0
while index < len(message_without_interference):
    if message_without_interference[index].isdigit():
        frequency += str(message_without_interference[index])
        index += 1
    elif index < len(message_without_interference):
        while not message_without_interference[index].isdigit():
            message += message_without_interference[index]
            index += 1
            if index == len(message_without_interference):
                break
        if int(frequency) > 100:
            final_message += message
        frequency = ""
        message = ""

print(final_message)
