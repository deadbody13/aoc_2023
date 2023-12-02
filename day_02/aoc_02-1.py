# sample = [
#         "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#         "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#         "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#         "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#         "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
#         ]

file = open("input_02-1.txt", "r")
contents = []
for x in file:
    contents.append(x)
file.close()

sum = 0
red_max = 12
green_max = 13
blue_max = 14
for x in contents:
    print(x)
    sets = x[x.index(":")+2:].split("; ")
    red_count = [int(y.split()[k-1]) for y in sets for k in range(len(y.split())) if y.split()[k] == "red" or y.split()[k] == "red,"]
    green_count = [int(y.split()[k-1]) for y in sets for k in range(len(y.split())) if y.split()[k] == "green" or y.split()[k] == "green,"]
    blue_count = [int(y.split()[k-1]) for y in sets for k in range(len(y.split())) if y.split()[k] == "blue" or y.split()[k] == "blue,"]
    if (max(red_count) <= red_max and max(green_count) <= green_max and max(blue_count) <= blue_max):
        game = x[:x.index(":")]
        sum += int(game.split()[1])

print(sum)
