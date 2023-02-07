from pprint import pprint
import re


def calculator(num1: int, num2: int, op: str):
    print(eval(f"{num1}{op}{num2}"))
    exec(f'print({num1}{op}{num2})')


s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ',
     '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']


def task2():
    global s
    cap_s = list(map(lambda data: data.capitalize(), s))
    print(*cap_s)


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


def task7_decorator(my_decorator):
    def get_name() -> str:
        name = input('Введите имя: ')
        my_decorator(name)
        return name
    return get_name


def greeting(name):
    print(f"Привет, {name}")


def task8_html(my_decorator):
    def parag(field) -> str:
        return f"<p>{my_decorator(field)}</p>"
    return parag


@task8_html
def render_input(field):
    return f'<input id="id_{field}" name="{field}">'


if __name__ == "__main__":
    print(render_input("login"))
    pass
