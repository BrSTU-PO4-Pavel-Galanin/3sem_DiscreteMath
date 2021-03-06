# Принимает параметр U, например, [1,2,3,4,5,6,7,8,9,10,11]
# Принимает параметр A, например, [1,3,4,7]
# Не возвращает значение
# Функция выведет в консоль булеан A
def boolean(U, A):
    power = 1 << len(A) # мощность множества A
    print("Boolean = P(%a) = 2^%d = {" % (A, power)) # Скобка открытия булеана

    for i in range(power):
        arr = []
        k = i # переведём итерацию цикла в двоичное число с помощью махинаций ниже
        for j in range(len(A)):
            arr.append( (int) (k % 2) ) # записываем 0 или 1
            k /= 2

        p = 0 # чтобы узнать сколько запятых
        for j in range(len(arr)):
            if arr[j] == 1:
                p += 1
        
        print("\t{", end = "") # скобка множества в булеане
        for j in range(len(arr)):
            if arr[j] == 1:
                p -= 1
                print(A[j], end = "")
                if p != 0:
                    print(", ", end = "")
        print("}", end = "") # закрытие скобки множества в булеане

        # Запятая после множества в булеане:
        if i != power - 1: # если это не последний элемент, то
            print(",") # вывести зщапятую
        else: # иначе
            print() # вывод конца строки

    print("}") # Скобка закрытия булеана
