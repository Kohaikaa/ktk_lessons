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
    position = 0
    for i in range(len(data)-1, 0, -1):
        if height <= data[i]:
            print(i+2)
            break
        elif i < 1:
            print(1)
            break


# Количество различных элементов
def task8():
    data = [int(i) for i in input().split()]
    data_set = set(data)
    print(len(data_set))


# Переставить соседние
def task9():
    data = [int(i) for i in input().split()]
    for i in range(1, len(data), 2):
        data[i-1], data[i] = data[i], data[i-1]
    for i in data:
        print(i, end=" ")


# Переставить min и max
def task10():
    data = [int(i) for i in input().split()]
    max_index = data.index(max(data))
    min_index = data.index(min(data))
    data[max_index], data[min_index] = data[min_index], data[max_index]
    for i in data:
        print(i)


# Удалить элемент
def task11():
    data = [int(i) for i in input().split()]
    k = int(input())
    data.pop(k)
    for i in data:
        print(i)


# Вставить элемент
def task12():
    data = [int(i) for i in input().split()]
    # Index, Element
    k, c = [int(i) for i in input().split()]
    data.insert(k, c)
    for i in data:
        print(i, end=" ")


# Количество совпадающих пар
def task13():
    data = [int(i) for i in input().split()]
    counter = 0
    for i in range(len(data)):
        k = 0
        while k + i + 1 < len(data):
            if data[i] == data[k + i + 1]:
                counter += 1
            k += 1
    print(counter)


# Уникальные элементы
def task14():
    data = [int(i) for i in input().split()]
    uniq_data = []
    for i in range(len(data)):
        k, counter = 0, 1
        while k < len(data):
            if data[i] == data[k] and i != k:
                counter += 1
            k += 1
        if counter == 1:
            uniq_data.append(data[i])
    print(" ".join([str(i) for i in uniq_data]))


# Кегельбан
def task15():
    N, K = [int(i) for i in input().split()]
    bahn = ["I"] * N
    for i in range(K):
        left, right = [int(j) for j in input().split()]
        for k in range(left - 1, right):
            bahn[k] = '.'
    print(''.join(bahn))


# Ферзи
def task16():
    class coordinates:
        def __init__(self, x, y) -> None:
            self.x = x
            self.y = y

    n = 8
    map = []
    for i in range(n):
        x, y = [int(i) for i in input().split()]
        map.append(coordinates(x, y))

    correct = True
    for i in range(n):
        for j in range(i+1, n):
            xStatement = map[i].x == map[j].x
            yStatement = map[i].y == map[j].y
            absStatement = abs(map[i].x - map[j].x) == abs(map[i].y - map[j].y)
            if xStatement or yStatement or absStatement:
                correct = False

    if not correct:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    task16()
