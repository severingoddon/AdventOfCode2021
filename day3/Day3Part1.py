def split(word):
    return [char for char in word]
with open('input.txt') as file:
    for line in file:

first, second, third, fourth, fifth, sixth, seventh, eight, ninth, tenth, eleventh, twelveth = [], [], [], [], [], [], [], [], [], [], [], []
bits = [first, second, third, fourth, fifth, sixth, seventh, eight, ninth, tenth, eleventh, twelveth]
gammaRate, epsilonRate = "", ""


        chars = split(line)
        chars.pop(len(chars) - 1)
        for i in range(len(chars)):
            bits[i].append(chars[i])

for i in range(len(bits)):
    gammaRate += max(set(bits[i]), key=bits[i].count)
    epsilonRate += min(set(bits[i]), key=bits[i].count)

print('Power consumption is: ', int(gammaRate, 2) * int(epsilonRate, 2))
