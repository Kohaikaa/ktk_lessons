# Количество различных чисел
def task1():
    nums = [int(i) for i in input().split()]
    nums_set = set(nums)
    print(len(nums_set))


# Количество совпадающих чисел
def task2():
    nums1 = [int(i) for i in input().split()]
    nums2 = [int(i) for i in input().split()]
    print(len(set(nums1) & set(nums2)))


# Пересечение множеств
def task3():
    nums1 = [int(i) for i in input().split()]
    nums2 = [int(i) for i in input().split()]
    nums = sorted(list(set(nums1) & set(nums2)))
    for i in nums:
        print(i)


# Встречалось ли число раньше
def task4():
    nums1 = [int(i) for i in input().split()]
    num_set = set()
    for i in nums1:
        if i in num_set:
            print("YES")
        else:
            print("NO")
            num_set.add(i)


# Кубики
def print_set(data):
    print(len(data))
    for i in sorted(list(data)):
        print(i, end=' ')


def task5():
    n, m = [int(i) for i in input().split()]
    anya, borya = set(), set()
    for i in range(0, n):
        anya.add(int(input()))
    for i in range(0, m):
        borya.add(int(input()))

    intersection_anya_set = anya & borya
    deff_anya_set = anya - borya
    deff_borya_set = borya - anya

    print_set(intersection_anya_set)
    print_set(deff_anya_set)
    print_set(deff_borya_set)


# Количество слов в тексте
def task6():
    lines_lim = int(input())
    text_set = set()
    for i in range(lines_lim):
        text_set.update(input().split())
    print(len(text_set))


# Угадай число
def task7():
    n = int(input())
    nums = set(range(1, n+1))
    true_nums = nums
    while True:
        question = input()
        if question == 'HELP':
            break
        question = {int(number) for number in question.split()}
        respond = input()
        if respond == "YES":
            true_nums &= question
        else:
            true_nums &= nums - question
    for i in sorted(list(true_nums)):
        print(i)


# Угадай число
def task8():
    n = int(input())
    nums = set(range(1, n+1))
    true_nums = nums
    while True:
        question = input()
        if question == 'HELP':
            break
        question = {int(number) for number in question.split()}
        # respond = input()
        if len(true_nums & question) > len(true_nums) / 2:
            print("YES")
            true_nums &= question
        else:
            print("NO")
            true_nums &= nums - question
    for i in sorted(list(true_nums)):
        print(i)


# Полиглот
def task9():
    people = int(input())
    all_languages = set()
    general_languages = set()
    for i in range(people):
        amount_of_langs = int(input())
        input_languages = set()
        for i in range(amount_of_langs):
            input_languages.add(input())
            all_languages |= input_languages
        general_languages = input_languages & all_languages

    def print_sets(data):
        print(len(data))
        for i in sorted(data):
            print(i)
    print_sets(general_languages)
    print_sets(all_languages)


# Забастовки
# Der Kampf - Борьба
# Die Arbeitstage - Будние дни
# Der Tag - день
def task10():
    # k - партия; n - дни
    n, k = [int(i) for i in input().split()]
    Arbeitstage = set(
        [Tag for Tag in range(1, n + 1)
         if Tag % 7 not in (6, 0)]
    )
    kein_kampf = set(Arbeitstage)
    for partei in range(k):
        a, b = [int(i) for i in input().split()]
        max_kampf = (n - a)
        kein_kampf -= {a + b*i for i in range(max_kampf)}
    print(len(Arbeitstage) - len(kein_kampf))


if __name__ == "__main__":
    task10()
