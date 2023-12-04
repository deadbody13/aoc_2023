# sample = [
#         "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
#         "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
#         "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
#         "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
#         "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
#         "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
#         ]
# content = sample

content = []
file = open("input_04-1.txt", "r")
for x in file:
    content.append(x)
file.close()


cards = 0
copies = []
for x in range(len(content)):
    match = 0
    card = content[x].split(":")[1].split("|")
    for y in card[0].split():
        if y in card[1].split():
            match += 1
    print(match)
    for y in range(match-1):
        copies.append(y+x+2)
    for z in copies:
        if (z == x+1):
            cards += 1
            for y in card[0].split():
                if y in card[1].split():
                    match += 1
            print(match)
            for y in range(match):
                copies.append(y+x+2)

print(cards)
