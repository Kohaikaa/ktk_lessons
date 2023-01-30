# Делаем срезы
def task1():
    line = input()
    print(line[2])
    print(line[-2])
    print(line[0:5])
    print(line[0:-2])
    print(line[::2])
    print(line[1::2])
    print(line[::-1])
    print(line[::-2])
    print(len(line))


# Количество слов
def task2():
    line = input()
    print(line.count(' ') + 1)


# Две половинки
def task3():
    line = input()
    middle = 0
    first_part, second_part = "", ""
    if len(line) % 2 == 0:
        middle = int(len(line) / 2)
    else:
        middle = int(len(line) / 2 + 1)
    first_part = line[0:middle]
    second_part = line[middle:]
    print(second_part+first_part)


# Переставить два слова
def task4():
    line = input()
    fp = line.split(' ')[0]
    sp = line.split(' ')[1]
    finish_line = sp + ' ' + fp
    print(finish_line)


# Первое и последнее вхождения
def task5():
    line = input()
    sum = line.count('f')
    if sum == 1:
        print(line.find('f'))
    elif sum > 1:
        print(line.find('f'), line.rfind('f'))


# Второе вхождение
def task6():
    line = input()
    sum = line.count('f')
    if sum == 1:
        print(-1)
    elif sum > 1:
        first_f = line.find('f')
        first_part_len = len(line[:first_f])+1
        print(line[first_f+1:].find('f')+first_part_len)
    else:
        print(-2)


# Удаление фрагмента
def task7():
    line = input()
    lines_to_replace = line[line.find('h'):line.rfind('h')]
    result = line.replace(lines_to_replace, "").replace('h', '')
    print(result)


# Обращение фрагмента
def task8():
    pass


# Замена подстроки
def task9():
    pass


# Удаление символа
def task10():
    pass


# Замена внутри фрагмента
def task11():
    pass


# Удалить каждый третий символ
def task12():
    pass


if __name__ == "__main__":
    task7()
