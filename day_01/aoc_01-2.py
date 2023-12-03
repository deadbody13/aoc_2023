def spelled_to_num(spelled_string):
    words =     ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    integers =  ["one1one",   "two2two",   "three3three",     "four4four",    "five5five",    "six6six",   "seven7seven",     "eight8eight",     "nine9nine"]
    # partial starts off as full string and is checked to see if it starts with a spelled-out number
    partial = spelled_string
    for x in range(len(spelled_string)):
        for y in range(len(words)):
            # check if partial starts with spelled-out word
            if (partial.startswith(words[y])):
                # replace only the first occurrence of that word in the original string
                spelled_string = spelled_string.replace(words[y], integers[y])
        # trim off leading letter from partial
        partial = partial[1:] 
    return spelled_string.split()

# put data into contents_spelled[], contains numbers spelled out
file = open("input_01-2.txt", "r")
contents_spelled = []
for x in file:
    contents_spelled += x.split()
file.close()

# # test data
# # answer: 281
# contents_spelled = [
#     "two1nine",
#     "eightwothree",
#     "abcone2threexyz",
#     "xtwone3four",
#     "4nineeightseven2",
#     "zoneight234",
#     "7pqrstsixteen"
# ]

# replace spelled numbers, put into contents[]
contents = []
for x in contents_spelled:
    contents += spelled_to_num(x)

# print replaced strings to output_1-2.txt
file = open("output_1-2.txt", "w")
for x in contents:
    file.write(x,)
    file.write("\n")
file.close()


# get numbers from strings and add to num_list[]
num_list = []
for x in contents:
    # add all numbers to str(number)
    num= ""
    for y in x:
        if y.isdigit():
            num+= y
    # concatenate first and last number
    num= num[0] + num[-1]
    num_list.append(int(num))

# add numbers together to get int(num_sum)
num_sum = 0
for x in num_list:
    num_sum += x
print(num_sum)
