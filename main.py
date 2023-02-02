from enum import Enum
from pprint import pprint


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


def reverse(sentence: str) -> str:
    return ''.join(i for i in sentence[::-1])


name_base = list()


def robot_hello(name: str) -> str:
    if name_base.count(name) > 0:
        return f"Привет, {name}!"
    name_base.append(name)
    return f"Привет, {name}! Рад знакомству!"


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


def Fibonacci_while():
    nums = [0, 1]
    while True:
        new_num = nums[-1] + nums[-2]
        if new_num > 100:
            break
        nums.append(new_num)
    pprint(nums)
    return nums


def Fibonacci_recorsion(num: int, fib_nums: list) -> int:
    if len(fib_nums) < 2:
        return
    if num >= 100:
        return fib_nums
    num = fib_nums[-1] + fib_nums[-2]
    fib_nums.append(num)
    num = Fibonacci_recorsion(num, fib_nums)
    return fib_nums


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

    # Task 5
    result = Fibonacci_recorsion([0, 1])
    pprint(result)
    pass
