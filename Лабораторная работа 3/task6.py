list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max = -2147483648
index = 0

for i in range(len(list_numbers)):
    if max < list_numbers[i]:
        max = list_numbers[i]
        index = i

indexOfLast = len(list_numbers)-1
list_numbers[index] = list_numbers[indexOfLast]
list_numbers[indexOfLast] = max

print(list_numbers)
