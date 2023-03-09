# Номер появления слова
def task1():
    my_dict = {}
    lst = [i for i in input().split(' ')]
    for i in lst:
        if i in my_dict:
            print(my_dict[i])
            my_dict[i] += 1
        else:
            print(0)
            my_dict[i] = 1


# Словарь синонимов
def task2():
    amount = int(input())
    dictionary = {}
    for i in range(amount):
        word, synonym = input().split()
        dictionary[word] = synonym
        dictionary[synonym] = word
    print(dictionary[input()])


# Выборы в США
def task3():
    amount_of_records = int(input())
    members = {}
    for i in range(amount_of_records):
        last_name, voices = input().split()
        voices = int(voices)
        if last_name in members:
            members[last_name] += voices
            continue
        members[last_name] = voices
    for last_name, voices in sorted(members.items()):
        print(last_name, voices)


# Самое частое слово
def task4():
    words = {}
    lines = int(input())
    for i in range(lines):
        line = input().split()
        for word in line:
            words[word] = words.get(word, 0) + 1
    max_count = max(words.values())
    most_frequent = [key for key, val in words.items() if val == max_count]
    print(min(most_frequent))


# Права доступа
def task5():
    history = []
    files_count = int(input())
    files_dict = {}
    for _file in range(files_count):
        # Вытаскиваем название файла и права
        _data = input().split()
        # Перебираем права
        access_rights = set()
        for right in range(1, len(_data)):
            access_rights.add(_data[right].lower())

        # Заполняем словарь
        files_dict[_data[0]] = access_rights

    operations_count = int(input())
    for operation in range(operations_count):
        command, file_name = input().split()
        # Проверяем доступ к файлу
        if command[0] in files_dict[file_name] or (command[1] == 'x') and command[1] in files_dict[file_name]:
            history.append("OK")
            continue
        history.append("Access denied")
    print('\n'.join(history))


# Частотный анализ
def task6():
    words = {}
    for i in range(int(input())):
        lines = input().split()
        for word in lines:
            words[word] = words.get(word, 0) + 1
    for word in sorted(words.items(), key=lambda x: (-x[1], x[0])):
        print(word[0])


# Страны и города
def task7():
    world = {}
    countries_count = int(input())
    for i in range(countries_count):
        line = input().split()
        country = line[0]
        cities = set()
        for index in range(1, len(line)):
            cities.add(line[index])
        world[country] = cities
    cities_count = int(input())
    for i in range(cities_count):
        city = input()
        for key, value in world.items():
            if city in value:
                print(key)


# Англо-латинский словарь
def task8():
    pass


# Контрольная по ударением
def task9():
    pass


# Продажи
def task10():
    pass


# Родословная: подсчет уровней
def task11():
    pass


# Родословная: предки и потомки
def task12():
    pass


# Родословная: LCA
def task13():
    pass


if __name__ == "__main__":
    task7()
