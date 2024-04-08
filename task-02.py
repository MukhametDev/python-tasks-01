try:
    number = int(input('Введите число от 1 до 20\n'))
    count = 1
    arr = []
    index = 0

    if number < 1 or number > 20:
        print('Введите корректное число')
    else:
        while count <= number:
            arr.append(count)
            count += 1

        for dig in range(len(arr)):
            dig = 0
            while dig != arr[index]:
                print('#', end="")
                dig += 1
            dig = 0
            index += 1
            print()

except ValueError:
    print('Ошибка: введено некорректное значение.')
