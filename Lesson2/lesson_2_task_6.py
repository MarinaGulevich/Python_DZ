lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

filtered_numbers = []
for num in lst:
    if num < 30 and num % 3 == 0:
        filtered_numbers.append(num)

print(filtered_numbers)
