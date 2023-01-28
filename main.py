# Список квадратов
def task1():
    n = int(input())
    result = 1
    i = 1
    while result <= n:
        print(result, end=' ')
        i += 1
        result = i ** 2


# Минимальный делитель
def task2():
    n = int(input())
    i = 2
    while n % i != 0:
        i += 1
    print(i)


# Степень двойки
def task3():
    n = int(input())
    grade = 1
    num = 2
    while num <= n:
        grade += 1
        num *= 2
    grade -= 1
    num = num // 2
    print(grade, num)


# Утренняя пробежка
def task4():
    x = int(input())
    y = int(input())
    days = 1
    while x < y:
        x += x * 10 / 100
        days += 1
    print(days)


# Длина последовательности
def task5():
    long_of_nums = 0
    while True:
        num = int(input())
        if num == 0:
            break
        long_of_nums += 1
    print(long_of_nums)


# Сумма последовательности
def task6():
    sum_of_nums = 0
    long_of_nums = 0
    while True:
        num = int(input())
        if num == 0:
            break
        sum_of_nums += num
        long_of_nums += 1
    result = sum_of_nums / long_of_nums
    print(result)


# Среднее значение последовательности
def task7():
    biggest_num = 0
    while True:
        num = int(input())
        if num == 0:
            break

        if num > biggest_num:
            biggest_num = num
    print(biggest_num)


# Максимум последовательности
def task8():
    biggest_num = 0
    i = 0
    biggest_num_index = 0
    while True:
        num = int(input())
        if num == 0:
            break

        if num > biggest_num:
            biggest_num = num
            biggest_num_index = i
        i += 1
    print(biggest_num_index)


# Индекс максимума последовательности
def task9():
    counter = 0
    while True:
        num = int(input())
        if num == 0:
            break
        if num % 2 == 0:
            counter += 1
    print(counter)


# Количество четных элементов последовательности
def task17():
    counter = 0
    while True:
        num = int(input())
        if num == 0:
            break
        if num % 2 == 0:
            counter += 1
    print(counter)


def task10():
    last_num = 0
    last_num_counter = 0
    while True:
        num = int(input())
        if num == 0:
            break
        if num > last_num:
            last_num_counter += 1
        last_num = num
    last_num_counter -= 1
    print(last_num_counter)


def task11():
    biggest_num = 0
    before_biggest_num = 0
    while True:
        num = int(input())
        if num == 0:
            break
        if num > biggest_num:
            before_biggest_num = biggest_num
            biggest_num = num
        elif num > before_biggest_num:
            before_biggest_num = num
    print(before_biggest_num)


# Количество элементов, равных максимуму
def task12():
    biggest_num = 0
    counter = 1
    while True:
        num = int(input())
        if num == 0:
            break
        if num > biggest_num:
            counter = 1
            biggest_num = num
        elif num == biggest_num:
            counter += 1
    print(counter)


# Числа Фибоначчи
def task13():
    second_num = 0
    first_num = 1
    current_num = 0
    n = int(input())
    i = 2
    if n == 0:
        print(0)
    else:
        while i <= n:
            second_num, first_num = first_num, first_num + second_num
            i += 1
        print(first_num)


# Номер числа Фибоначчи
def task14():
    n = int(input())
    if n <= 0:
        print(0)
    else:
        last_num = 0
        new_num = 1
        i = 1
        while new_num < n:
            current_num = new_num + last_num
            last_num = new_num
            new_num = current_num
            i += 1
        if new_num == n:
            print(i)
        else:
            print(-1)


# Максимальное число идущих подряд равных элементов
def task15():
    counter, biggest_counter = 1, 1
    last_num = 0
    while True:
        n = int(input())
        if n == 0:
            break
        if n == last_num:
            counter += 1
            if counter > biggest_counter:
                biggest_counter = counter
        else:
            counter = 1
        last_num = n
    print(biggest_counter)


# Стандартное отклонение
# result = sqrt(pow(x-s, 2) / n - 1)
def task16():
    from math import sqrt
    partial_sum = 0
    partial_sum_squares = 0
    x_i = int(input())
    n = 0
    while x_i != 0:
        n += 1
        partial_sum += x_i
        partial_sum_squares += x_i ** 2
        x_i = int(input())
    result = sqrt((partial_sum_squares - partial_sum ** 2 / n) / (n - 1))
    print(result)


if __name__ == "__main__":
    task16()
