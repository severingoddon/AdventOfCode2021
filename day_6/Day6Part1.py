valuesBeforeShift = []
day_counters = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}


def countDay():
    for day, fish_count in day_counters.items(): valuesBeforeShift.append(fish_count)
    for x in range(len(day_counters)):
        if x == 8:
            day_counters[8] = valuesBeforeShift[0]
            day_counters[6] += valuesBeforeShift[0]
        else: day_counters[x] = valuesBeforeShift[x + 1]
    valuesBeforeShift.clear()


with open('input.txt') as file:
    for file_line in file:
        fishTimers = file_line.split(",")
        for timer in fishTimers: day_counters[int(timer)] += 1

for i in range(80): countDay()

sum_of_fish = 0
for key, value in day_counters.items(): sum_of_fish += value
print(sum_of_fish)
