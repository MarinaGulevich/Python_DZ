from Python_HWk.Lesson2.lesson_2_task_1 import result


def is_year_leap(number):
    return True if number % 4 == 0 else False


num = int(input("Ввeдите год:"))

result = is_year_leap(num)

print(f"Год: {num}: - {result}")
