# Лабораторная №1. Выполнил: студент БСТ2203 Парфенов Никита Алексеевич
# _______________________________________________________________________#

import random
import time
import copy

##########################################################

# Задание 1

# print("Hello, World!")


#############################################################


# Задание 2
# Введем необходимые параметры


# m = int(input())
# n = int(input())
# min_lim = int(input())
# max_lim = int(input())
#
# pre_matrix = []
# matrix = []
#
# for i in range(0, n):
#     for j in range(0, m):
#         pre_matrix.append(random.randint(min_lim, max_lim)) # генерация элемента

#         # далее прописан переход на следующую строку:
#         # если размер вектора-строки равна измерению m
#         # то pre_matrix добавляется в matrix, а затем обнуляется
#
#         if len(pre_matrix) == m:
#             matrix.append(pre_matrix)
#             pre_matrix = []
# print(matrix)


#####################################################################


# Задание 3

# Используем параметры из предыдущего задания
print("Количество столбцов: ")
n = int(input())  # количество столбцов
print("Количество строк: ")
m = int(input())  # количество строк
print("Минимум генерации: ")
min_lim = int(input())  # минимум генерации
print("Максимум генерации: ")
max_lim = int(input())  # максимум генерации

# Используем генератор для создания матрицы

main_matrix = [[random.randint(min_lim, max_lim) for i in range(m)] for j in range(n)]  # оригинальная матрица

# Сделаем копии матрицы для каждой из сортировок

main_matrix_or = copy.deepcopy(main_matrix)  # копия для создании других массивов
main_matrix_choice_sorting = copy.deepcopy(main_matrix_or)  # для сортировки выбором
main_matrix_insert_sorting = copy.deepcopy(main_matrix_or)  # для сортировки вставкой
main_matrix_bubble_sorting = copy.deepcopy(main_matrix_or)  # для сортировки пузырьком
main_matrix_shell_sorting = copy.deepcopy(main_matrix_or)  # для сортировки Шелла
main_matrix_quick_sorting = copy.deepcopy(main_matrix_or)  # для быстрой сортировки
main_matrix_tournament_sorting = copy.deepcopy(main_matrix_or)  # для турнирной сортировки

# --------------сортировка методом sorted-----------------------------------------------

# Сложность: O(n log n)

print("Начальная матрица (ф-ция sorted):", main_matrix)

start = time.perf_counter()  # начало теста сортировки встроенной функцией sorted

for i in range(len(main_matrix)):
    main_matrix[i] = sorted(main_matrix[i])

finish = time.perf_counter() - start  # конец теста сортировки встроенной функцией sorted

print("Конечная матрица (ф-ция sorted):", main_matrix)
print("--- {0} mcs ---".format(round((finish) * 1000000)))  # в микросекнудах

# -------------------сортировка выбором-------------------------------------------------------------

# Сложность: O(n^2)
print("Начальная матрица (choice sorting):", main_matrix_choice_sorting)

start_sorting_choice = time.perf_counter()  # старт теста сортировки выбором

lowest_index = -1  # создадим переменную, в которой будем хранить индекс текущего элемента

for i in range(len(main_matrix_choice_sorting)):  # каждый из подсписков сортируем по отдельности
    for j in range(len(main_matrix_choice_sorting[i])):
        lowest_index = j
        for p in range(j + 1, len(main_matrix_choice_sorting[i])):
            if main_matrix_choice_sorting[i][p] < main_matrix_choice_sorting[i][lowest_index]:
                lowest_index = p

        main_matrix_choice_sorting[i][j], main_matrix_choice_sorting[i][lowest_index] = main_matrix_choice_sorting[i][
            lowest_index], main_matrix_choice_sorting[i][j]

finish_sorting_choice = time.perf_counter() - start_sorting_choice  # конец теста сортировки выбором

print("Конечный массив (choice sorting):", main_matrix_choice_sorting)
print("--- {0} mcs ---".format(round((finish_sorting_choice) * 1000000)))  # в микросекнудах

# -------------------сортировка вставкой-----------------------------------------------

# Сложность: O(n^2)
print("Начальная матрица (insert sorting):", main_matrix_insert_sorting)

start_sorting_insert = time.perf_counter()  # начало теста сортировки вставкой

now_index = -1

# Пройдем с помощью цикла всю матрицу:
# Каждый элемент будем двигать с помощью уменьшения индекса на 1
# вплоть до того, пока он не станет больше текущего элемента

for i in range(len(main_matrix_insert_sorting)):
    for j in range(len(main_matrix_insert_sorting[i])):
        for p in range(j + 1, len(main_matrix_insert_sorting[i])):
            now_index = p
            while main_matrix_insert_sorting[i][p] < main_matrix_insert_sorting[i][j]:
                main_matrix_insert_sorting[i][j], main_matrix_insert_sorting[i][p] = main_matrix_insert_sorting[i][p], \
                    main_matrix_insert_sorting[i][j]
                p -= 1

finish_sorting_insert = time.perf_counter() - start_sorting_insert  # конец теста сортировки вставкой

print("Конечная матрица (insert sorting):", main_matrix_insert_sorting)
print("--- {0} mcs ---".format(round((finish_sorting_insert) * 1000000)))  # в микросекнудах

# ---------------сортировка пузырьком--------------------------------------------------------------

# Сложность: O(n^2)
print("Начальная матрица (bubble sorting):", main_matrix_bubble_sorting)

start_sorting_bubble = time.perf_counter()  # старт сортировки пузырьком

for i in range(len(main_matrix_bubble_sorting)):
    for j in range(len(main_matrix_bubble_sorting[i])):
        for p in range(len(main_matrix_bubble_sorting[i]) - 1):
            if main_matrix_bubble_sorting[i][p + 1] < main_matrix_bubble_sorting[i][p]:
                main_matrix_bubble_sorting[i][p], main_matrix_bubble_sorting[i][p + 1] = main_matrix_bubble_sorting[i][
                    p + 1], main_matrix_bubble_sorting[i][p]

finish_sorting_bubble = time.perf_counter() - start_sorting_bubble  # конец теста сортировки пузырьком

print("Конечная матрица (bubble sorting):", main_matrix_bubble_sorting)
print("--- {0} mcs ---".format(round((finish_sorting_bubble) * 1000000)))  # в микросекнудах

# ------------сортировка Шелла------------------------------------------------

# Сложность: O(n log^2 n)
print("Начальная матрица (Shell's sorting):", main_matrix_shell_sorting)

start_sorting_shell = time.perf_counter()  # начало теста сортировки Шелла

coefficent = 2
# Будем делить длину каждого под списка на 2
# чтобы уменьшать диапазоны между сравниваемыми значениями
while m != 0:
    for i in range(len(main_matrix_shell_sorting)):
        for j in range(len(main_matrix_shell_sorting[i])):
            for p in range(j + (m // coefficent), len(main_matrix_shell_sorting[i])):
                if main_matrix_shell_sorting[i][j] > main_matrix_shell_sorting[i][p]:
                    main_matrix_shell_sorting[i][j], main_matrix_shell_sorting[i][p] = main_matrix_shell_sorting[i][p], \
                        main_matrix_shell_sorting[i][j]
    m //= coefficent

finish_sorting_shell = time.perf_counter() - start_sorting_shell

print("Конечная матрица (Shell's sorting):", main_matrix_shell_sorting)
print("--- {0} mcs ---".format(round((finish_sorting_shell) * 1000000)))

# ------------Быстрая сортировка-----------------------------------------

# Сложность: O(n log n) - O(n^2)
print("Начальная матрица (quick sorting):", main_matrix_quick_sorting)


# Напишем функцию для быстрой сортировки

def quick_sorting(massiv):
    if len(massiv) < 2:  # если строка состоит из 1 элемента - просто её возвращаем
        return massiv
    low_massiv, equal_massiv, high_massiv = [], [], []  # разделим на три части строку для удобства сортировки

    base_elem = massiv[0]  # за базовый элемент возьмем первый элемент

    # разделим строку на три списка

    for i in range(len(massiv)):
        if massiv[i] > base_elem:
            high_massiv.append(massiv[i])
        elif massiv[i] == base_elem:
            equal_massiv.append(massiv[i])
        else:
            low_massiv.append(massiv[i])

    # Возвращать рекурсивно будем отсортированные списки больших и меньших элементов
    # соединённых с списком элементов, равных базовому

    return quick_sorting(low_massiv) + equal_massiv + quick_sorting(high_massiv)


start_sorting_quick = time.perf_counter()  # начало теста быстрой сортировки

for i in range(len(main_matrix_quick_sorting)):
    main_matrix_quick_sorting[i] = quick_sorting(main_matrix_quick_sorting[i])

finish_sorting_quick = time.perf_counter() - start_sorting_quick  # конец теста быстрой сортировки

print("Конечная матрица (quick sorting):", main_matrix_quick_sorting)
print("--- {0} mcs ---".format(round((finish_sorting_quick) * 1000000)))

# -------турнирная сортировка--------------

# Сложность: O(n log^2 n)

print("Начальная матрица (tournament sorting):", main_matrix_tournament_sorting)


def tour_sort(arr, n):
    loosers = []
    winners = []  # создадим списки победителей и проигравших

    def tree(arr, n):  # турнирное дерево№
        left = arr[0]  # первый конкурсант
        right = arr[1]  # второй конкурсант
        for i in range(2, n):
            current = arr[i]  # потенциально победитель
            if left < current:
                current, left = left, current  # другое значение побеждает
            if right <= current:
                current, right = right, current  # другое значение побеждает
            check(current)
        check(left)  # когда закончились текущие, оставшиеся проходят проверку
        check(right)
        return winners, loosers

    def check(element):  # проверка на включение в победители или проигравшие
        if len(winners) == 0 or (len(winners) != 0 and element >= max(winners)):
            winners.append(element)
        else:
            loosers.append(element)
        return winners, loosers

    def sum(loosers, winners):  # сложение списков
        arr2 = []
        winners_length = len(winners)
        loosers_length = len(loosers)
        if loosers_length == 0:  # если нет проигравших, возвращаем победителей
            return winners
        for i in range(winners_length + loosers_length):
            now_elem = min(winners[0], loosers[0])  # берем мнимаильный из двух списков
            arr2.append(now_elem)  # добавляем в результирующий массив
            if winners[0] == now_elem:
                winners.pop(0)  # если элемент из победителей, то убираем его из массива и длину на 1 уменьшаем
                winners_length -= 1
            else:
                loosers.pop(0)
                loosers_length -= 1

            if winners_length == 0:
                arr2.extend(loosers)
                break
            if loosers_length == 0:
                arr2.extend(winners)
                break
        return arr2

    tree(arr, len(arr))
    if (loosers[i] > loosers[i + 1] for i in range(0, len(loosers) - 1)):
        arr = loosers
        arr.extend(winners)  # добавление победителей в общий список
        loosers = []
        winners = []
        arr = tree(arr, len(arr))
    arr = sum(loosers, winners)
    return arr


start_sorting_tournament = time.perf_counter()  # начало теста турнирной сортировки

for i in range(n):
    main_matrix_tournament_sorting[i] = tour_sort(main_matrix_tournament_sorting[i], m)

finish_sorting_tournament = time.perf_counter() - start_sorting_tournament  # конец теста турнирной сортировки
print("Конечная матрица (tournament sorting):", main_matrix_tournament_sorting)
print("--- {0} mcs ---".format(round((finish_sorting_tournament) * 1000000)))

############################################################################################

# Вывод:
# В ходе л/р, я вспомнил синтаксис языка Python, написал алгоритм генерации матрицы,
# алгоритмы сортировок встроенной функции sorted, выбором, вставкой, пузырьком,
# Шелла, быстрой и турнирной. Привёл сравнение скоростей работы алгоритмов.
# Могу также заявить, что скорость алгоритмов зависит от количества поданных данных -
# одни алгоритмы быстрее других при маленьком объеме поступающих данных, но при большом
# объеме они гораздо медленнее (например, сравнивая сортировки пузырьком и быструю), поэтому, можно
# однозначно сказать: при маленьком количестве поступающих чисел, можно использовать одни алгоритмы,
# при большом - другие, более эффективные.
