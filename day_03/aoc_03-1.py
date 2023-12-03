def isSpecial(char):
    if (char.isdigit() is False and char != "." and char != "\n"):
        return True
    else:
        return False


# sample = ["467..114..",
#           "...*......",
#           "..35..633.",
#           "......#...",
#           "617*......",
#           ".....+.58.",
#           "..592.....",
#           "......755.",
#           "...$.*....",
#           ".664.598.."
#           ]
# content = sample

content = []
file = open("input_03-1.txt", "r")
for x in file:
    content.append(x)
file.close()

sum = 0
numberof = 0
for x in range(len(content)):
    numberof += 1
    y = 0
    # for _ in range(len(content[x])):
    while (y < len(content[x])):
        number = ""
        hasSpecial = False
        while (content[x][y].isdigit()):
            number += content[x][y]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    try:
                        if (isSpecial(content[x+i][y+j])):
                            hasSpecial = True
                    except:
                        pass
            y += 1
        if (hasSpecial):
            print(number)
            sum += int(number)
            hasSpecial = False
        y += 1
print(sum)
print(numberof)
