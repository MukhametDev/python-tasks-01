number = '124143243456546'
even_sum = 0
odd_sum = 0

for digit in number:
    if int(digit) % 2 == 0:
        even_sum += int(digit)
    else:
        odd_sum += int(digit)

print(f'Сумма нечетных чисел: {odd_sum} Сумма четных чисел: {even_sum}')
