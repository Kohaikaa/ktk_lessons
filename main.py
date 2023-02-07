from pprint import pprint
import re


def calculator(num1: int, num2: int, op: str):
    # Причина ненавидеть Python №1: много малоиспользуемых функций.
    print(eval(f"{num1}{op}{num2}"))
    exec(f'print({num1}{op}{num2})')


s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ',
     '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']


def task2():
    global s
    cap_s = list(map(lambda data: data.capitalize(), s))
    print(*cap_s)


# Причина ненавидеть Python №2: несмотря на динамическое определение типа,
# приходится указывать тип данных, чтобы видеть, какие ф-ции доступны.
def task3_honest(data: list) -> list:
    return list(filter(lambda x: x % 2 == 0, data))


def task4_cesar():
    line = input()
    cesar_line: str = ''
    for i in line:
        cesar_line += chr(ord(i) + 3)
    return cesar_line


def task5_countdown(data: list):
    data = sorted(data, reverse=True)
    for i in data:
        print(i)
    print("Пуск")


def task6_alphabet():
    lch = [chr(x) for x in range(ord('a'), ord('z'))]
    hch = [chr(x) for x in range(ord('A'), ord('Z'))]
    alphabet = hch + lch
    al_dict = dict()
    for i in alphabet:
        al_dict[i] = ord(i)
        print(f'{ord(i)} - {i}')

    # Dictionary output
    pprint(al_dict)


# Причина ненавидеть Python №3: извращенные декораторы.
def task7_decorator(my_decorator):
    def get_name() -> str:
        name = input('Введите имя: ')
        my_decorator(name)
        return name
    return get_name


def greeting(name):
    print(f"Привет, {name}")


# Даже пробовать не буду дальше

# def task8_html(my_decorator):
#     def parag(field) -> str:
#         print("<p>", end='')
#         my_decorator(field)
#         print("</p>")
#     return parag


# @task8_html
# def render_input(field):
#     return f'<input id="id_{field}" name="{field}">'

if __name__ == "__main__":
    # decorated = task7_decorator(greeting)
    # decorated()
    pass
