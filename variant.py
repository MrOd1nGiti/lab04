n = int(input("Введите количество чисел n: "))

count = 0
total_sum = 0

for i in range(1, n + 1):
    num = int(input(f"Введите число {i}: "))
    if num % 2 == 0:
        count += 1
        total_sum += num

print(f"Количество подходящих чисел: {count}")
print(f"Сумма подходящих чисел: {total_sum}")

print()
check_num = int(input("Введите целое число n >= 2 для проверки на простоту: "))
is_prime = True
divisor = 2

while divisor * divisor <= check_num:
    if check_num % divisor == 0:
        is_prime = False
        break
    divisor += 1

if is_prime:
    print(f"Число {check_num}: простое")
else:
    print(f"Число {check_num}: составное")
