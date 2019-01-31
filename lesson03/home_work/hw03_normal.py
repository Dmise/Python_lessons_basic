# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

print("Задача 1 - Функция, возвращающая ряд фибоначи. (Запишу все в лист)")


def fibonacci(n, m):
    fibonacci_seq = [1, 1]
    counter = 2
    if n > m or n < 0 or m < 0:
        print("Ты мне втираешь какую-то дичь")
    if m > 2:
        while counter < m:
            fibonacci_seq.append(fibonacci_seq[counter - 1] + fibonacci_seq[counter - 2])
            counter += 1
    return fibonacci_seq[n - 1:m]


print(fibonacci(2, 5))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print("Задача 2 -")


def sort_to_max(origin_list):
    list_len = len(origin_list)
    counter = 0
    swap_amount_peritteration = 0
    while counter < list_len - 1:
        if origin_list[counter] > origin_list[counter + 1]:
            temp = origin_list[counter]
            origin_list[counter] = origin_list[counter + 1]
            origin_list[counter + 1] = temp
            swap_amount_peritteration += 1
            # print('Swap')
        counter += 1
        if counter == list_len - 1:
            if swap_amount_peritteration == 0:
                print(origin_list)  # это я для проверки.  запутался децл.
                return origin_list
            else:
                # заходим на новый круг... обнуляем счетчики
                swap_amount_peritteration = 0
                counter = 0


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

print("Задача 3 ")

def my_filter(function, seq):
    new_list = []
    for elem in seq:
        if function(elem):
            new_list.append(elem)
    return new_list

print(my_filter((lambda x: x >2), [1,2,2,2,3,34,45,0]))  # вроде бы работает, но без обработки исключений.

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print("Задача-4: из данных точек сделаю векторы A1-A2,  A2-A3, A3-A4, A4-A1, другого способа образования прямых не рассматриваю, например А1-А3, A3-A4, A4-A2, A2-A1")
A1 = [0, 0]
A2 = [1, 0]
A3 = [1, 1]
A4 = [0, 1]


def is_parallelogramm(a, b, c, d):
    vecA = create_vector(a, b)
    vecB = create_vector(b, c)
    vecC = create_vector(c, d)
    vecD = create_vector(d, a)
    if is_perpendicular(vecA, vecB):
        if is_perpendicular(vecB, vecC):
            if is_perpendicular(vecC, vecD):
                if is_perpendicular(vecD, vecA):
                    return True
    else:
        return False

def create_vector(a, b):
    vector = []
    vector.append(b[0] - a[0])
    vector.append(b[1] - a[1])
    return vector


def is_perpendicular(a, b):
    if a[0] * b[0] + a[1] * b[1] == 0:
        return True
    else:
        return False


print(is_parallelogramm(A1, A2, A3, A4))
