import copy

data, data2 = [], []
lengthOfChars = 0


def convert(s):
    new = ""
    for x in s: new += x
    return new


def split(word):
    return [x for x in word]


def findCommonBit(data_list, index):
    listOfCurrentBits = []
    common_Bit = 0
    for row in data_list:
        listOfCurrentBits.append(row[index])
    zeroCount = listOfCurrentBits.count("0")
    oneCount = listOfCurrentBits.count("1")
    if zeroCount > oneCount: common_Bit = "0"
    if zeroCount < oneCount: common_Bit = "1"
    if zeroCount == oneCount:
        common_Bit = "1"
    return common_Bit


def calculate(data_list, lookingForOxygen):
    for i in range(lengthOfChars):
        if len(data_list) > 1:
            common_Bit = findCommonBit(data_list=data_list, index=i)
            new_data = []
            for row in data_list:
                if lookingForOxygen:
                    if row[i] == common_Bit: new_data.append(row)
                else:
                    if row[i] != common_Bit: new_data.append(row)
            data_list.clear()
            data_list = copy.deepcopy(new_data)
        else:
            break
    return data_list


with open('input.txt') as file:
    for line in file:
        chars = split(line)
        if len(chars) > 12:
            chars.pop(len(chars) - 1)
        data.append(chars)
        data2.append(chars)
    lengthOfChars = len(chars)

oxygen_generator_rating = calculate(data, lookingForOxygen=True)
co2_scrubber_rating = calculate(data2, lookingForOxygen=False)

print(int(convert(oxygen_generator_rating[0]), 2) * int(convert(co2_scrubber_rating[0]), 2))
