def task1():
    num = int(input())
    print(num % 10)


def task2():
    speed = int(input())
    mtime = int(input())
    distance = 109
    result = int(speed * mtime % distance)
    print(result)


def task3():
    num = float(input())
    result = num % 1
    print(result)


def task4():
    num = float(input())
    result = int((num - int(num)) * 10 % 10)
    print(result)


def task5():
    num = int(input())
    result = (num * 45 + (num // 2) * 5 + ((num + 1) // 2 - 1) * 15)
    hours = result // 60 + 9
    minutes = result % 60
    print(hours, minutes)


def task6():
    from math import ceil
    n = int(input())
    m = int(input())
    days = ceil(m / n)
    print(days)


def task7():
    rub = int(input())
    kops = int(input())
    n = int(input())
    price = (rub * 100 + kops) * n
    print(int(price // 100), price % 100)


def task8():
    h1 = int(input())
    m1 = int(input())
    s1 = int(input())

    h2 = int(input())
    m2 = int(input())
    s2 = int(input())

    total_sec1 = h1 * 3600 + m1 * 60 + s1
    total_sec2 = h2 * 3600 + m2 * 60 + s2
    result = total_sec2 - total_sec1
    print(result)


def task9():
    from math import ceil
    h = int(input())
    a = int(input())
    b = int(input())

    result = ceil((h - a) / (a - b)) + 1
    print(result)


def task10():
    num = int(input())
    result = int(num % 100 / 10)
    print(result)


def task11():
    pass


def task12():
    pass


def task13():
    pass


def task14():
    pass


def task15():
    pass


def task16():
    pass


if __name__ == '__main__':
    task3()
