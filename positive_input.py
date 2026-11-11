attempts = 0
number = int(input("Введите положительное число: "))

while number <= 0:
    attempts += 1
    number = int(input("Неверно. Введите положительное число: "))

square = number ** 2

print(f"Квадрат числа: {square}")
print(f"Количество отклонённых попыток: {attempts}")
