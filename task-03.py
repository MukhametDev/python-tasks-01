try:
    number = int(input('Введите число от 1 до 100\n'))
    arr = []
    for i in range(100):
        arr.append(i)
    low = 0
    high = len(arr) - 1
    check = ''
    if number >=1 and number <=100:
        while low <= high:
            indx = (low + high) // 2
            desired_number = arr[indx]
            check = input(f'Число равно: {desired_number}.Напиши "Больше", "Меньше" или "Верно"\n')
            if check.upper() == 'БОЛЬШЕ':
                low = indx + 1
            elif check.upper() == 'МЕНЬШЕ':
                high = indx - 1
            elif check.upper() == 'ВЕРНО':
                print(f'Ваше число: {desired_number}')
                break
            else:
                print('Вывели некорретное значение!')
                break

except ValueError:
    print('Некорректное значение')