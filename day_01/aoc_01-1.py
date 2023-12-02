file = open("input.txt", "r")
contents = []
for x in file:
    contents += x.split()
file.close()

strings_num = []
for x in contents:
    number = ""
    for y in x:
        if y.isdigit():
            number += y
    if (len(number) == 1):
        number += number
    number = number[0] + number[-1]
    strings_num.append(number)
print(strings_num)

string_sum = 0
for x in strings_num:
    string_sum += int(x)
print(string_sum)