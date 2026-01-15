def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


num = int(input("Ввeдите год:"))

result = is_year_leap(num)

print(f"Год: {num}: - {result}")
