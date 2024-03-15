# Лабораторная №2. Выполнил: студент БСТ2203 Парфенов Никита Алексеевич
# _______________________________________________________________________#

from StackDack import Deque

# from StackDack import Stack

# from StackDack import Stack

# Задание 1

# Отсортировать строки файла, содержащие названия книг, в алфавитном порядке с использованием двух деков.


# -----------------------------------------------------------------------

# Создадим два дека
# deque_1 = Deque()
# deque_2 = Deque()
#
# with open("myfile.txt", 'r', encoding='utf-8') as file:
#     strs = file.readlines()
# for line in strs:
#     deque_1.push_bottom(line)  # добавим все элементы файла в первый дэк
#
#
# while not (deque_1.is_empty()):
#     elem = deque_1.pop_top()
#     while not deque_2.is_empty() and deque_2.pop_bottom() < elem:
#         deque_1.push_top(deque_2.pop_bottom())
#     deque_2.push_bottom(elem)
#
#
# deque_1.show_deque()
# -------------------------------------------------------------------------

# Задание 7

# Дан файл из целых чисел.
# Используя дек, за один просмотр файла напечатать сначала все отрицательные числа,
# затем все положительные числа,
# сохраняя исходный порядок в каждой группе.

numbers = Deque()
with open("number_for_7.txt", 'r', encoding='utf-8') as file:
    nums = file.readlines()
    for line in nums:
        num = int(line)
        if num < 0:
            numbers.push_bottom(num)
        if num > 0:
            numbers.push_top(num)

    numbers.show_deque()

numbers.show_deque()

# -------------------------------------------------------------------------
# Задание 8

# Дан текстовый файл.
# Используя стек, сформировать новый текстовый файл,
# содержащий строки исходного файла, записанные в обратном порядке:
# первая строка становится последней, вторая – предпоследней и т.д.

# ------------------------------------------------------------------------

# stack = Stack()  # создадим стек
# with open("myfile.txt", 'r', encoding="utf-8") as file:
#     strs = file.readlines()  # прочитаем файл
#
# for line in strs:
#     stack.push(line)  # запишем строки в стек
#
# with open("myfile_sorted_8.txt", 'w', encoding="utf-8") as file:  # запишем строки в файл
#     while not stack.is_empty():
#         elem = stack.cut()
#         file.write(elem)
