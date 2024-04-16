import random
import BinarySearchTree_Class as bt
import networkx as nx
import time


# ------------------- functions

def menu():
    print("1 - Добавить элемент")
    print("2 - Удалить элемент")
    print("3 - Поиск элемента")

    user_request = input("<?>: ")
    if user_request in ["1", " 1"]:
        print()
        print("1 - Генерация элемента")
        print("2 - Ввод элемента")
        user_request_1 = input("<?>: ")
        if user_request_1 in ["1", " 1"]:
            print()
            data.append(random.randint(-100000, 10000))
            print(data)
            print()
            menu()
        elif user_request_1 in ["2", " 2"]:
            print()
            data.append(int(input("<?>: ")))
            print()
            print(data)
            print()
            menu()
        else:
            print()
            print("_InputError_")
            print()
            time.sleep(3)
            menu()
    elif user_request in ["2", " 2"]:
        print()
        print("1 - Удаление по конкретному индексу")
        print("2 - Удаление конкретного элемента")
        user_request_1 = input("<?>: ")
        if user_request_1 in ["1", " 1"]:
            print()
            data.pop(int(input("<?> ")))
            print()
            print(data)
            print()
            menu()
        elif user_request_1 in ["2", " 2"]:
            print()
            data.remove(int(input("<?>: ")))
            print()
            print(data)
            print()
            menu()
        else:
            print()
            print("_InputError_")
            print()
            time.sleep(3)
            menu()
    elif user_request in ["3", " 3"]:
        print()
        print("1 - Встроенный метод")
        print("2 - Линейный поиск")
        print("3 - Бинарный поиск")
        print("4 - Интерполяционный поиск")
        print("5 - Фибоначчиев поиск")
        print("6 - Бинарное дерево")
        print()
        user_request_1 = input("<?>: ")
        if user_request_1 == "1" or user_request_1 == " 1":
            print()
            want_to_find = int(input("Введите элемент, который необходимо найти: "))
            if data.count(want_to_find) == 1:
                t = time.perf_counter()
                print()
                print("Элемент найден. Индекс элемента: ", data.index(want_to_find))
                t1 = time.perf_counter() - t
                print()
                print("Время работы алгоритма: ", t1 * 1000)
                print()
                menu()
            elif data.count(want_to_find) > 1:
                t = time.perf_counter()
                print()
                print("Найдено ", data.count(want_to_find), " желаемых элементов.")
                t1 = time.perf_counter() - t
                print("Индексы элементов: ", [i for i in range(len(data)) if data[i] == want_to_find])
                print()
                print("Время работы алгоритма: ", t1 * 1000)
                print()
                menu()
            else:
                print()
                print("Элемент отсутствует в дампе данных.")
                print()
                menu()
        elif user_request_1 == "2" or user_request_1 == " 2":
            print()
            want_to_find = int(input("Введите элемент, который необходимо найти: "))
            print()
            t = time.perf_counter()
            for elem in range(len(data)):
                if data[elem] == want_to_find:
                    print("Элемент найден по индексу: ", elem)
            t1 = time.perf_counter() - t
            print()
            print("Время работы алгоритма: ", t1 * 1000)
            print()
            menu()
        elif user_request_1 == "3" or user_request_1 == " 3":
            print()
            want_to_find = int(input("Введите число, которое неободимо найти: "))
            print()
            operations = 0
            binary_search(data, want_to_find, operations)
            print()
            menu()
        elif user_request_1 == "4" or user_request_1 == " 4":
            sort_data = sorted(data)
            print("Отсортированный массив:", sort_data)
            print()
            print("Введите значение, которое необходимо найти: ")
            print()
            want_to_find = int(input("<?>: "))
            print()
            print("Элемент найден по индексу:", interpole_search(sort_data, want_to_find))
            print()

            menu()
        elif user_request_1 == "5" or user_request_1 == " 5":
            print()
            want_to_find = int(input("Введите число, которое необходимо найти: "))
            print()
            sort_data = sorted(data)
            print("Отсортированный массив:", sort_data)
            print()
            t = time.perf_counter()
            i = fibonachi_search(sort_data, want_to_find, len(sort_data))
            if i >= 0:
                print("Элемент найден по индексу:", i)
                t1 = time.perf_counter() - t
                print()
                print("Время работы алгоритма:", t1 * 1000)
            else:
                print("Элемент не найден в дампе данных.")
                t1 = time.perf_counter() - t
                print()
                print("Время работы алгоритма:", t1 * 1000)
        elif user_request_1 == "6" or user_request_1 == " 6":
            print()
            want_to_find = int(input("Введите число, которое необходимо найти: "))
            print()
            bst = bt.BinarySearchTree()
            for element in data:
                bst.insert(element)
            print()
            res = bst.search(want_to_find)
            if res is None:
                print("Значение не найдено в дереве")
                print()
                menu()
            else:
                print("Значение найдено.")
                print("Выполняю отрисовку...3..2..1")
                time.sleep(3)
                bst.visualize()
                print()
                menu()



    else:
        print()
        print("_InputError_")
        print()
        time.sleep(1)
        menu()


def binary_search(data, element, operations):
    t = time.perf_counter()
    operations += 1
    sort_data = sorted(data)
    print("Отсортированный список: ", sort_data)
    low_half = [sort_data[i] for i in range(0, len(sort_data) // 2 + 1)]
    high_half = [sort_data[i] for i in range(len(sort_data) // 2 + 1, len(sort_data))]
    print("1-ая: ", low_half)
    print("2-ая: ", high_half)
    print()
    if element not in sort_data:
        print("Проверьте корректность введённых данных.")
        print()
        menu()
    elif low_half[-1] == element:
        print("Элемент найден по индексу:", sort_data.index(element), "за", operations, "операций.")
        print()
        print("Время работы алгоритма: ", (time.perf_counter() - t) * 1000)
        print()
        menu()
    elif low_half[-1] > element:
        binary_search(low_half, element, operations)
        print()
    elif low_half[-1] < element:
        if high_half[-1] == element:
            print("Элемент найден по индексу:", sort_data.index(element), "за ", operations, "операций.")
            print()
            print("Время работы алгоритма: ", (time.perf_counter() - t) * 1000)
            print()
            menu()
        elif high_half[-1] > element:
            binary_search(high_half, element, operations)
            print()


def interpole_search(sort_data, element):
    t = time.perf_counter()
    print()
    left_side = 0
    right_side = len(sort_data) - 1
    while sort_data[left_side] < element and element < sort_data[right_side]:
        important = left_side + (element - sort_data[left_side]) * (right_side - left_side) // (
                sort_data[right_side] - sort_data[left_side])
        if sort_data[important] < element:
            left_side = important + 1
        elif sort_data[important] > element:
            right_side = important - 1
        else:
            t1 = time.perf_counter() - t
            print("Время работы алгоритма:", t1 * 1000)
            return important
    if sort_data[left_side] == element:
        t1 = time.perf_counter() - t
        print("Время работы алгоритма:", t1 * 1000)
        return left_side
    elif sort_data[right_side] == element:
        t1 = time.perf_counter() - t
        print("Время работы алгоритма:", t1 * 1000)
        return right_side
    else:
        print()
        return "None"


def fibonachi_search(massiv, element, n):
    q = 0  # previous for previous
    p = 1  # previous for fibonhachi number
    fibonachi_number = q + p

    while fibonachi_number < n:
        p, q = fibonachi_number, p
        fibonachi_number = p + q

    elim = -1  # marks cutted range

    while fibonachi_number > 1:
        index = min(elim + q, n - 1)
        if massiv[index] < element:
            fibonachi_number = p
            p = q
            q = fibonachi_number - p
            elim = index
        elif massiv[index] > element:
            fibonachi_number = q
            p -= q
            q = fibonachi_number - p
        else:
            return index

    if (p and massiv[n - 1] == element):
        return n - 1

    return -1


##############################


data = []

for _ in range(10):  # creating data dump
    data.append(random.randint(-10000, 10000))

print(data)
print()
menu()
