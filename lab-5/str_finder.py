import time

stroch = "ImagineThatIsAText"


def kmp_search(text, pattern):
    massiv_suffix_prefix = [0] * len(pattern)
    j = 0
    i = 1
    while i < len(pattern):
        if pattern[j] == pattern[i]:
            massiv_suffix_prefix[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                massiv_suffix_prefix[i] = 0
                i += 1
            else:
                j = massiv_suffix_prefix[j - 1]

    i = 0
    j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - len(pattern)
        elif text[i] != pattern[j]:
            if j > 0:
                j = pattern[j - 1]
            else:
                i += 1

    if i == len(text):
        return -1


def bmr_search(text, pattern):
    n = len(pattern)
    bad_char_positions = [n - 1] * 256
    for i in range(n - 1):
        bad_char_positions[ord(pattern[i])] = n - 1 - i

    skipping = 0
    massiv = tuple()
    while len(text) - skipping >= n:
        if text[skipping:skipping + n] == pattern:
            massiv = (skipping, skipping + n)
        skipping += bad_char_positions[ord(text[skipping + n - 1])]

    if not len(massiv):
        return -1

    return massiv


def menu(register):
    global stroch
    print("Строка:", stroch)
    print("--------------------------")
    print()
    print("1 - Добавить символы в строку")
    print("2 - Изменить строку")
    print("3 - Чувствительность к регистру")
    print("4 - Запустить поиск")

    user_request = input("<?>: ")
    if user_request in ["1", " 1"]:
        print()
        want_to_add = input("Введите символы, которые хотите добавить:")
        print()
        stroch = stroch + want_to_add
        print(stroch + want_to_add)
        menu(register)
    elif user_request in ["2", " 2"]:
        print()
        want_to_add = input("Введите строку:")
        print()
        stroch = want_to_add
        menu(register)
    elif user_request in ["3", " 3"]:
        print()
        print("1 - Включить")
        print("2 - Выключить")
        user_request_1 = input("<?>: ")
        if user_request_1 in ["1", " 1"]:
            register = True
            print("Чувствительность к регистру: включена", "(", register, ")")
            print()
            menu(register)
        elif user_request_1 in ["2", " 2"]:
            register = False
            print("Чувствительность к регистрру: выключена", "(", register, ")")
            print()
            menu(register)
        else:
            print("InputErr")
            print()
            menu(register)
    elif user_request in ["4", " 4"]:
        print()
        print("1 - Встроенная функция")
        print("2 - Алгоритм Кнута-Морриса-Пратта")
        print("3 - Упрощённый алгоритм Бойера-Мура")
        user_request_2 = input("<?>: ")
        if user_request_2 in ["1", " 1"]:
            print()
            want_to_find = input("Введите строку, которую желаете найти: ")
            print()
            t = time.perf_counter()
            if register:
                if want_to_find in stroch:
                    print("Строка найдена. Находится в диапазоне между",
                          stroch[stroch.index(want_to_find[0]) - 1], "и", stroch[stroch.index(want_to_find[-1]) + 1])
                    print()
                    print("Время выполнения:", (time.perf_counter() - t) * 1000)
                    print()
                    menu(register)
                else:
                    print("Строка не найдена. Возможно, из-за чувствительности регистра.")
                    print()
                    print("Время выполнения:", (time.perf_counter() - t) * 1000)
                    print()
                    menu(register)

            elif not register:
                if want_to_find in stroch.upper() or want_to_find in stroch.lower() or want_to_find in stroch:
                    print("Строка найдена. Находится в диапазоне между",
                          stroch[stroch.index(want_to_find[0]) - 1], "и", stroch[stroch.index(want_to_find[-1]) + 1])
                    print()
                    print("Время выполнения:", (time.perf_counter() - t) * 1000)
                    print()
                    menu(register)
                else:
                    print("Строка не найдена. Возможно, из-за чувствительности регистра.")
                    print()
                    print("Время выполнения:", (time.perf_counter() - t) * 1000)
                    print()
                    menu(register)
        elif user_request_2 in ["2", " 2"]:
            print()
            want_to_find = input("Введите строку, которую желаете найти: ")
            t = time.perf_counter()
            print()
            if not register:
                print("Строка найдена по индексу:", kmp_search(stroch, want_to_find))
                print()
                print("Время работы алгоритма:", (time.perf_counter() - t) * 1000)
                print()
                menu(register)
            elif register:
                if want_to_find.isupper():
                    print("Строка найдена по индексу:", kmp_search(stroch, want_to_find.upper()))
                    print()
                    print("Время работы алгоритма:", (time.perf_counter() - t) * 1000)
                    print()
                    menu(register)
                elif want_to_find.islower():
                    print("Строка найдена по индексу:", kmp_search(stroch, want_to_find.lower()))
                    print()
                    print("Время работы алгоритма:", (time.perf_counter() - t) * 1000)
                    print()
                    menu(register)
                else:
                    print("Строка найдена по индексу:", kmp_search(stroch.lower(), want_to_find))
                    print()
                    print("Время работы алгоритма:", (time.perf_counter() - t) * 1000)
                    print()
                    menu(register)
        elif user_request_2 in ["3", " 3"]:
            print()
            want_to_find = input("Введите строку, которую желаете найти:")
            t = time.perf_counter()
            print()
            if not register:
                print("Строка найдена в промежутке:", bmr_search(stroch, want_to_find))
                print()
                print("Время работы алгоритма:", (time.perf_counter() - t) * 1000)
                print()
                menu(register)
            elif register:
                if want_to_find.isupper():
                    print("Строка найдена в промежутке:", bmr_search(stroch, want_to_find.upper()))
                    print()
                    print("Время работы алгоритма:", (time.perf_counter() - t) * 1000)
                    print()
                    menu(register)
                elif want_to_find.islower():
                    print("Строка найдена в промежутке:", bmr_search(stroch, want_to_find.lower()))
                    print()
                    print("Время работы алгоритма:", (time.perf_counter() - t) * 1000)
                    print()
                    menu(register)
                else:
                    print("Строка найдена в промежутке:", bmr_search(stroch.lower(), want_to_find))
                    print()
                    print("Время работы алгоритма:", (time.perf_counter() - t) * 1000)
                    print()
                    menu(register)

    else:
        print("InputErr")
        print()
        menu(register)


register = False
menu(register)
