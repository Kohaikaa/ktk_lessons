from random import randint
from enum import Enum
from pprint import pprint


# Task 1 start
class Operations(Enum):
    addition = 1
    subtraction = 2
    multiply = 3
    division = 4


def calculator(num1: int, num2: int, operation: Operations):
    if operation == Operations.addition:
        return num1 + num2
    if operation == Operations.subtraction:
        return num1 - num2
    if operation == Operations.multiply:
        return num1 * num2
    if operation == Operations.division:
        if num2 == 0:
            print("Error! Division on zero is not possible")
            return 0
        return num1 / num2
# Task 1 end


# Task 2 start
def reverse(sentence: str) -> str:
    return ''.join(i for i in sentence[::-1])
# Task 2 end


# Task 3 start
name_base = list()


def robot_hello(name: str) -> str:
    global name_base
    if name_base.count(name) > 0:
        return f"Привет, {name}!"
    name_base.append(name)
    return f"Привет, {name}! Рад знакомству!"
# Task 3 end


# Task 4 start
def count_while():
    i = 0
    while i <= 10:
        print(i, end=" ")
        i += 1


def count_recursion(num):
    print(num, end=" ")
    if num == 10:
        return num
    result = count_recursion(num + 1)
    return result
# Task 4 end


# Task 4* start
def count_odd_even_while():
    count_odd, count_even = 0, 0
    i = 0
    while i <= 10:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        i += 1
    print(f"Четные: {count_even}\nНечетные: {count_odd}")


def count_odd_even_recursion(index=0, counter_even=0, counter_odd=0):
    if index > 10:
        print(f"Четные: {counter_even}\nНечетные: {counter_odd}")
        return

    if index % 2 == 0:
        counter_even += 1
    else:
        counter_odd += 1
    count_odd_even_recursion(index + 1, counter_even, counter_odd)
# Task 4* end


# Task 5 start
def Fibonacci_while():
    nums = [0, 1]
    while True:
        new_num = nums[-1] + nums[-2]
        if new_num > 100:
            break
        nums.append(new_num)
    return nums


def Fibonacci_recorsion(fib_nums: list):
    if fib_nums[-1] > 100 or len(fib_nums) < 2:
        fib_nums.pop(-1)
        return
    new_num = fib_nums[-1] + fib_nums[-2]
    fib_nums.append(new_num)
    Fibonacci_recorsion(fib_nums)
    return fib_nums
# Task 5 end


# Task 6 start
def factorial_while(n):
    fact = 1
    while n >= 1:
        fact *= n
        n -= 1
    return fact


def factorial_recursion(n):
    if n <= 1:
        return 1
    n *= factorial_recursion(n-1)
    return n
# Task 6 end


# Task 7 start
db = dict()


def login():
    global db
    loginn = input("Your login: ")
    password = input("Your password: ")
    if loginn not in db:
        db[loginn] = password
        print("Registretion was successful!")
        return

    if loginn in db:
        if db.get(loginn) == password:
            print("Доступ разрешен")
            return
        print("Доступ запрещен")
# Task 7 end


# Task 8 start
def game(bot_num=0, attempts=10):
    if attempts <= 0:
        print(
            f"Кончились попытки, увы, вы проиграли. Это было число {bot_num}")
        return
    answer = int(input("Я думаю это число "))
    if answer == bot_num:
        print(f"Вы угадали, это число {bot_num}")
        return

    if answer > bot_num:
        print("Ваше число больше загаданного числа.", end=" ")
    elif answer < bot_num:
        print("Ваше число меньше загаданного числа.", end=" ")
    print(f"Осталось {attempts - 1} попыток.")
    game(bot_num, attempts - 1)
# Task 8 end


if __name__ == "__main__":
    # Task 1
    # result = calculator(25, 0, Operations.division)
    # print(result)

    # Task 2
    # result = reverse("Hello, World!")
    # print(result)

    # Task 3
    # result = robot_hello("Vlad")
    # print(result)

    # result = robot_hello("Dima")
    # print(result)

    # result = robot_hello("Angelina")
    # print(result)

    # result = robot_hello("Vlad")
    # print(result)

    # result = robot_hello("Angelina")
    # print(result)

    # Task 4
    # count_while()
    # num = 0
    # count_recursion(num)

    # Task 4*
    # count_odd_even_while()
    # count_odd_even_recursion()

    # Task 5
    # pprint(Fibonacci_while())
    # result = Fibonacci_recorsion([3, 5])
    # pprint(result)

    # Task 6
    # print(factorial_while(5))
    # print(factorial_recursion(5))

    # Task 7
    # login()
    # login()
    # login()

    # Task 8
    bot_num = randint(0, 100)
    print("Бот загадал число, отгадай.")
    game(bot_num)
