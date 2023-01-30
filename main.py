# Четные индексы
def task1():
    data = input().split()
    for i in range(0, len(data), 2):
        print(data[i])


# Четные элементы
def task2():
    data = input().split()
    for i in data:
        if int(i) % 2 == 0:
            print(i)


# Больше предыдущего
def task3():
    data = [int(i) for i in input().split()]
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            print(data[i], end=" ")


# Соседи одного знака
def task4():
    data = [int(i) for i in input().split()]
    for i in range(1, len(data)):
        if data[i-1] * data[i] > 0:
            print(data[i-1], data[i])
            break


# Больше своих соседей
def task5():
    data = [int(i) for i in input().split()]
    counter = 0
    for i in range(1, len(data)-1):
        if data[i-1] < data[i] and data[i] > data[i+1]:
            counter += 1
    print(counter)


# Наибольший элемент
def task6():
    data = [int(i) for i in input().split()]
    print(max(data), data.index(max(data)))


# Шеренга
def task7():
    data = [int(i) for i in input().split()]
    height = int(input())
    for i in range(len(data)):
        if data[i] < height:
            print(i+1)
            break


# Количество различных элементов
def task8():
    pass


# Переставить соседние
def task9():
    pass


# Переставить min и max
def task10():
    pass


# Удалить элемент
def task11():
    pass


# Вставить элемент
def task12():
    pass


# Количество совпадающих пар
def task13():
    pass


# Уникальные элементы
def task14():
    pass


# Кегельбан
def task15():
    pass


# Ферзи
def task16():
    pass


if __name__ == "__main__":
    task3()
