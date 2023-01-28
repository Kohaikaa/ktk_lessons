def task1():
    n = int(input())
    result = 1
    i = 1
    while result <= n:
        print(result, end=' ')
        i += 1
        result = i ** 2


def task2():
    n = int(input())
    i = 2
    while n % i != 0:
        i += 1
    print(i)


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


def task4():
    x = int(input())
    y = int(input())
    days = 1
    while x < y:
        x += x * 10 / 100
        days += 1
    print(days)


def task5():
    long_of_nums = 0
    while True:
        num = int(input())
        if num == 0:
            break
        long_of_nums += 1
    print(long_of_nums)


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


def task7():
    biggest_num = 0
    while True:
        num = int(input())
        if num == 0:
            break

        if num > biggest_num:
            biggest_num = num
    print(biggest_num)


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


def task9():
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


def task14():
    second_num = 0
    first_num = 1
    current_num = 0
    n = int(input())
    i = 2
    if n == 0:
        print(0)
    else:
        while first_num <= n:
            if first_num == n:
                print(i)
                break
            elif first_num >= n:
                print(-1)
                break
            current_num = first_num + second_num
            second_num = first_num
            first_num = current_num
            i += 1
        print(first_num)


def task15():
    pass


def task16():
    pass


def task17():
    pass


if __name__ == "__main__":
    task12()
