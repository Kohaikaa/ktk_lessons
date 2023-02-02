def task1():
    a = int(input())
    b = int(input())
    for i in range(a, b+1):
        print(i, end=' ')


def task2():
    a = int(input())
    b = int(input())
    if a < b:
        for i in range(a, b+1):
            print(i, end=' ')
    elif a > b:
        for i in range(a, b-1, -1):
            print(i, end=' ')
    else:
        print(a)


def task3():
    a = int(input())
    b = int(input())
    for i in range(a-(a+1) % 2, b-b % 2, -2):
        print(i, end=' ')


def task4():
    result = 0
    for i in range(10):
        num = int(input())
        result += num
    print(result)


def task5():
    nums = int(input())
    result = 0
    for i in range(nums):
        result += int(input())
    print(result)


def task6():
    from math import pow
    nums = int(input())
    result = 0
    for i in range(1, nums+1):
        result += int(pow(i, 3))
    print(result)


def task7():
    n = int(input())
    result = 1
    for i in range(1, n+1):
        result *= i
    print(result)


def task8():
    n = int(input())
    fac_mul = 1
    fac_sum
    for i in range(1, n+1):
        fac_mul *= i
        fac_sum += fac_mul
    print(fac_sum)


def task9():
    n = int(input())
    result = 0
    for i in range(n):
        num = int(input())
        if num == 0:
            result += 1
    print(result)


def task10():
    n = int(input())
    last_num = 0
    for i in range(1, n+1):
        last_num += i
        print(last_num)
        last_num *= 10


def task11():
    n = int(input())
    sum = 0
    for i in range(1, n + 1):
        sum += i
    for i in range(n - 1):
        sum -= int(input())
    print(sum)


if __name__ == "__main__":
    task11()
