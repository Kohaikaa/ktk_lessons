def task1():
    a = int(input())
    b = int(input())
    c = int(input())
    sum = a + b + c
    print(sum)


def task2():
    b = int(input())
    h = int(input())
    result = 1/2 * b * h
    print(result)


def task3():
    n = int(input())  # Students
    k = int(input())  # Apples
    students = int(k / n)
    card = int(k % n)
    print(students)
    print(card)


def task4():
    n = int(input())
    hour = n % (60 * 24) // 60
    minutes = n % 60
    print(hour, minutes)


def task5():
    name = input()
    print(f"Hello, {name}")


def task6():
    num = int(input())
    print("The next number for the number " + str(num) + " is " + str(num + 1))
    print("The previous number for the number " +
          str(num) + " is " + str(num - 1))


def task7():
    a = int(input())
    b = int(input())
    c = int(input())
    sum = int(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)
    print(sum)


def task8():
    a = int(input())
    b = int(input())
    l = int(input())
    n = int(input())
    result = (a * n + b*(n-1) + l) * 2 - a
    print(result)


if __name__ == '__main__':
    task6()
