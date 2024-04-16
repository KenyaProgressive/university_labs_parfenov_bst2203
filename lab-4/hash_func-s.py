import hashlib
import random
import chains_method_class as h

# Простое перехэщирование

# n = int(input("Введите длину хэш-таблицы: "))
# hash_table = [None] * n
#
#
# def hash_function(key):
#     return key % n
#
#
# def insert(key, value):
#     index = hash_function(key)
#     while hash_table[index] is not None:
#         index = (index + 1) % n
#     hash_table[index] = value
#
#
# for i in range(5):
#     hash_table.insert(random.randint(-100, 100), i)

# ----------------------------------------------------

# Рехэширование с псевдослучайными числами

# Создаем список чисел
# numbers = [random.randint(-4375, 3814) for i in range(0, random.randint(15, 456))]
# # Создаем новый список для хранения перехешированных чисел
# new_numbers = []
# # Перебираем числа из исходного списка
# for number in numbers:
#     # Генерируем псевдослучайное число в диапазоне от 0 до 100
#     random_number = random.randint(15, 100)
#     # Перехешируем число с помощью псевдослучайного числа
#     hashed_number = (number * random_number) % len(numbers)
#     # Добавляем перехешированное число в новый список
#     new_numbers.append(hashed_number)
# # Выводим исходный список и список перехешированных чисел
#
#
# print("Исходный список чисел:", numbers)
# print("Перехешированный список чисел:", new_numbers)

# ----------------------------------------------------

# Метод цепочек

hash = h.HashTable()
for i in range(100):
    hash.add(i // 2, i ** 2)

print(hash.get(45))
