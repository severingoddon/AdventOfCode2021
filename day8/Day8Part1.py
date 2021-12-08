with open('input.txt') as file:
    count = 0
    for file_line in file:
        splitted = file_line.split(" | ")
        values = splitted[1].split()
        for v in values:
            if len(v) == 2 or len(v) == 3 or len(v) == 4 or len(v) == 7: count += 1
print(count)
