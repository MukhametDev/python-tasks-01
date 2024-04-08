try:
    number = input('Введите число от 0 до 10^20\n')
    even_sum = 0
    odd_sum = 0

    number = int(number)

    if 0 <= number <= 10**20:
        for digit in str(number):
            if int(digit) % 2 == 0:
                even_sum += int(digit)
            else:
                odd_sum += int(digit)

        print(f'Сумма нечетных чисел: {odd_sum} Сумма четных чисел: {even_sum}')
    else:
        print("Число должно быть в диапазоне от 0 до 10^20.")
except ValueError:
    print("Ошибка: введено неверное значение.")
except KeyboardInterrupt:
    print("Процесс прерван.")
