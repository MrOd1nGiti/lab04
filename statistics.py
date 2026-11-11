n = int(input("Введите количество чисел n: "))

if n > 0:
    first_num = int(input("Введите число 1: "))
    total_sum = first_num
    positive_count = 1 if first_num > 0 else 0
    max_num = first_num

    for i in range(2, n + 1):
        num = int(input(f"Введите число {i}: "))
        total_sum += num
        if num > 0:
            positive_count += 1
        if num > max_num:
            max_num = num

    print(f"Сумма: {total_sum}")
    print(f"Положительных: {positive_count}")
    print(f"Максимум: {max_num}")
