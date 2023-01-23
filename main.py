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
    num = int(input())
    n1 = num % 10
    n2 = int(num % 100 / 10)
    n3 = int(num / 100)
    result = n1 + n2 + n3
    print(n1, n2, n3, result)


def task12():
    from math import sqrt
    k1 = int(input())
    k2 = int(input())
    result = int(sqrt(k1 ** 2 + k2 ** 2))
    print(result)


def task13():
    h = int(input())
    m = int(input())
    s = int(input())
    result = h * 30 + m * 30 / 60 + s * 30 / 3600
    print(result)


def task14():
    a = float(input())
    result = a % 30 * 12
    print(result)


def task15():
    angle = float(input())
    hours = int(angle // 30)
    minutes = int(angle % 30 * 2)
    seconds = int(angle % 0.5 * 120)
    print(hours, minutes, seconds)


def task16():
    p = int(input())
    x = int(input())
    y = int(input())
    money_before = 100 * x + y
    money_after = int(money_before * (100 + p) / 100)
    rubles = money_after // 100
    kops = money_after % 100
    print(rubles, kops)


if __name__ == '__main__':
    task11()
