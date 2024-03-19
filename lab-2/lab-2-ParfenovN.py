# Лабораторная №2. Выполнил: студент БСТ2203 Парфенов Никита Алексеевич
# _______________________________________________________________________#

from StackDack import Deque
from StackDack import Stack
import string

# Задание 1

# Отсортировать строки файла, содержащие названия книг, в алфавитном порядке с использованием двух деков.

# deque_1 = Deque()
# deque_1_1 = Deque()
#
# with open("myfile.txt", 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#     for line in lines:
#         deque_1.add_rear(line)
#
#     while not deque_1.is_empty():
#         element = deque_1.pop_rear()
#         while not deque_1_1.is_empty() and deque_1_1.peek_rear() > element:
#             deque_1.add_front(deque_1_1.pop_rear())
#         deque_1_1.add_rear(element)
#
# with open("myfile.txt", 'w', encoding='utf-8') as file:
#     while not deque_1_1.is_empty():
#         element_ = deque_1_1.pop_front()
#         file.write(element_)

# -----------------------------------------------------------------------

# Создадим два дека

# -------------------------------------------------------------------------

# Задание 2

# Дек содержит последовательность символов для шифровки сообщений.
# Дан текстовый файл, содержащий зашифрованное сообщение.
# Пользуясь деком, расшифровать текст.
# Известно, что при шифровке
# каждый символ сообщения заменялся следующим за
# ним в деке по часовой стрелке через один.

deque_2 = Deque()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in alphabet:
    deque_2.add_rear(char)  # добавим алфавит в дек
res = ""

with open("file2.txt", 'r',
          encoding="utf-8") as file:
    mes = file.read()
    for char in mes:
        while char != deque_2.peek_front():  # пока символ сообщения не совпадет с символом алфавита
            # переносим символы из начала в конец.
            deque_2.add_rear(deque_2.pop_front())
        deque_2.add_front(deque_2.pop_rear())
        res += deque_2.peek_front()
# print(res)

with open("file2.txt", 'w', encoding="utf-8") as file:
    file.write(res)
# -------------------------------------------------------------------------
# Задание 3


# Даны три стержня и n дисков различного размера.
# Диски можно надевать на стержни, образуя из них башни.
# Перенести n дисков со стержня А на стержень С, сохранив их первоначальный порядок.
# При переносе дисков необходимо соблюдать следующие правила:
# - на каждом шаге со стержня на стержень переносить только один диск;
# - диск нельзя помещать на диск меньшего размера;
# - для промежуточного хранения можно использовать стержень В.
# Реализовать алгоритм, используя три стека вместо стержней А, В, С.
# Информация о дисках хранится в исходном файле.

first = Stack()  # Башня 1
second = Stack()  # Башня 2
third = Stack()  # Башня 3
helper = 0  # для конвертации информации о дисках в числа


# def hanoi_tower_task(n, from_tower, help_tower, to_tower):
#     if n == 1:
#         elem = from_tower.pop()
#         to_tower.push(elem)
#         print(f"Перемещаем {elem}")
#     else:
#         hanoi_tower_task(n - 1, from_tower, help_tower, to_tower)
#         elem = from_tower.pop()
#         to_tower.push(elem)
#         print(f"Перемещаем {elem}")
#
# with open("file3.txt", 'r', encoding="utf-8") as file:
#     disks = file.readlines()
#
# for i in range(len(disks)):
#     helper = int(disks[i])
#     disks[i] = helper
#
# for i in disks:
#     first.push(i)
#
# hanoi_tower_task(len(disks), first, second, third)
#
# first.show()
# second.show()
# third.show()

# ---------------------------------------------------------------------------

# Задание 4

# Дан текстовый файл с
# программой на алгоритмическом языке.
# За один просмотр файла проверить баланс
# круглых скобок в тексте, используя стек.

# stack_4 = Stack()
# skobka_counter = 0
# with open("file4.txt", 'r', encoding="utf-8") as file:
#     strs = file.readlines()
#     for line in strs:
#         for i in range(len(line)):
#             stack_4.push(line[i])
#             if stack_4.peek() == "(":
#                 skobka_counter += 1
#             elif stack_4.peek() == ")":
#                 skobka_counter -= 1
#     if skobka_counter == 0:
#         print("Баланс скобок сохраняется")
#     else:
#         print("Баланс скобок нарушен")

# -------------------------------------------------------------------------

# Задание 5
# Дан текстовый файл с программой на алгоритмическом языке.
# За один просмотр файла проверить
# баланс квадратных скобок в тексте, используя дек.

# deque_5 = Deque()
# deque_skobka_counter = 0
#
# with open("file5.txt", 'r', encoding="utf-8") as file:
#     strs_ = file.readlines()
#     for line in strs_:
#         for i in range(len(line)):
#             if line[i] == "[":
#                 deque_5.add_front(line[i])
#                 deque_skobka_counter += 1
#             elif line[i] == "]":
#                 deque_5.add_rear(line[i])
#                 deque_skobka_counter -= 1
#     if deque_skobka_counter == 0:
#         print('Баланс скобок сохраняется')
#     else:
#         print('Баланс скобок нарушен')

# ------------------------------------------------------------------------

# Задание 6
# Дан файл из символов.
# Используя стек, за один просмотр файла напечатать сначала все цифры,
# затем все буквы, и, наконец, все остальные символы,
# сохраняя исходный порядок в каждой группе символов.

# stack_6 = Stack()
# with open("file6.txt", 'r+', encoding="utf-8") as file:
#     strs__ = file.readlines()
#     strs__ = strs__[::-1] # перевернём, чтобы при внесении сохранить изначальный порядок файла
#     for line in strs__: # запишем в конец символы
#         for i in range(len(line)):
#             if not line[i].isdigit() and not line[i].isalpha() and line[i] != "\n":
#                 stack_6.push(line[i])
#     for line in strs__: # в середину буквы
#         for i in range(len(line)):
#             if line[i].isalpha():
#                 stack_6.push(line[i])
#     for line in strs__: # в начало цифры
#         for i in range(len(line)):
#             if line[i].isdigit():
#                 stack_6.push(line[i])
#     file.write("\n")
#     file.write("\n")
#     file.write("===================================================")
#     file.write("\n")
#     file.write("\n")
#     while not stack_6.is_empty():
#         el = stack_6.pop()
#         file.write(el)
#         file.write("\n")

# -------------------------------------------------------------------------
# Задание 7
# Дан файл из целых чисел.
# Используя дек, за один просмотр файла напечатать
# сначала все отрицательные числа, затем все положительные числа,
# сохраняя исходный порядок в каждой группе.

# deque_7a = Deque()
# with open("number_for_7.txt", 'r', encoding="utf-8") as file:
#     strs = file.readlines()
#     for line in strs:
#         num = int(line)
#         if num < 0:
#             deque_7a.add_rear(num)
#     for line in strs:
#         num = int(line)
#         if num > 0:
#             deque_7a.add_rear(num)
#     while not deque_7a.is_empty():
#         el = deque_7a.pop_front()
#         print(el)

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
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
#     stack.push(line.strip())  # запишем строки в стек, удаляя лишние пробелы
#
# with open("myfile_sorted_8.txt", 'w', encoding="utf-8") as file:  # запишем строки в файл
#     while not stack.is_empty():
#         elem = stack.pop()
#         file.write(elem)
#         file.write("\n")
