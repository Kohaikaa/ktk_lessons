def task1():
    a = int(input())
    b = int(input())
    if a > b:
        print(b)
    else:
        print(a)


def task2():
    num = int(input())
    if num > 0:
        print(1)
    elif num < 0:
        print(-1)
    else:
        print(0)


def task3():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    sq1 = (a+b) % 2
    sq2 = (c+d) % 2
    if sq1 == sq2:
        print("YES")
    else:
        print("NO")


def task4():
    n = int(input())
    if n % 4 == 0 and not n % 100 == 0 or n % 400 == 0:
        print("YES")
    else:
        print("NO")


def task5():
    a = int(input())
    b = int(input())
    c = int(input())

    if a <= b and a <= c:
        print(a)
    elif b <= a and b <= c:
        print(b)
    else:
        print(c)


def task6():
    a = int(input())
    b = int(input())
    c = int(input())
    if a == b and a == c:
        print(3)
    elif a == b and a != c or b == c and a != b or a == c and b != c:
        print(2)
    else:
        print(0)


def task7():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if a == c or b == d:
        print("YES")
    else:
        print("NO")


def task8():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    stepX = (x1-x2)
    stepY = (y1 - y2)
    if abs(stepX) <= 1 and abs(stepY) <= 1:
        print("YES")
    else:
        print("NO")


def task9():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    stepX = (x1-x2)
    stepY = (y1 - y2)
    if abs(stepX) == abs(stepY):
        print('YES')
    else:
        print('NO')


def task10():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    stepX = (x1-x2)
    stepY = (y1 - y2)
    if abs(stepX) == abs(stepY) or x1 == x2 or y1 == y2:
        print('YES')
    else:
        print('NO')


def task11():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        print('YES')
    else:
        print('NO')


def task12():
    n = int(input())
    m = int(input())
    k = int(input())
    if k < n * m and ((k % n == 0) or (k % m == 0)):
        print('YES')
    else:
        print('NO')


def task13():
    n = int(input())
    m = int(input())
    x = int(input())
    y = int(input())

    if n > m:
        n, m = m, n
    if x >= n / 2:
        x = n - x
    if y >= m / 2:
        y = m - y
    if x < y:
        print(x)
    else:
        print(y)


if __name__ == "__main__":
    pass
