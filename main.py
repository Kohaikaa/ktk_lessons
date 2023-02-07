import re


def task1_validator():
    try:
        num = int(input("Enter your number: "))
        return num ** 2
    except Exception as ex:
        print("Error!")
        return -1


def task2_check():
    line = input("Note here: ")
    if len(re.findall(r'[!@#$%^&*]', line)) >= 1:
        raise ValueError
    return line


def find_email(line: str):
    return re.findall(r'\S+@\S+\.\S+', line)


if __name__ == '__main__':
    line = 'Всем привет! Меня зовут Алексей. Мой email: alexVB@gmail.com. Привет, Алексей! Меня зовут Марина, моя почта: Marina@mail.ru'
    result = find_email(line)
    print(' '.join(result))
