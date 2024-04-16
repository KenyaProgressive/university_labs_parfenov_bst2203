from collections import defaultdict
import time as t

stroch = "ImagineThatIsAText"


def menu():
    global stroch
    register = False
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
        print(stroch + want_to_add)
        menu()
    elif user_request in ["2", " 2"]:
        print()
        want_to_add = input("Введите строку:")
        print()
        stroch = want_to_add
        menu()
    elif user_request in ["3", " 3"]:
        print()
        print("1 - Включить")
        print("2 - Выключить")
        user_request_1 = input("<?>: ")
        if user_request_1 in ["1", " 1"]:
            print("Чувствительность к регистру: включена")
            register = True
            menu()
        elif user_request_1 in ["2", " 2"]:
            print("Чувствительность к регистрру: выключена")
            register = False
            menu()
        else:
            print("InputErr")
            print()
            menu()


menu()
