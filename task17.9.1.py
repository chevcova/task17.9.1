array = [int(x) for x in input("Введите числа в любой последовательности, через пробел: ").split()]

def merge_sort(array):  # "разделяй"
    if len(array) < 2:  # если кусок массива равен 2,
        return array[:]  # выход из рекурсии
    else:
        middle = len(array) // 2  # ищем середину
        left = merge_sort(array[:middle])  # рекурсивно делим левую часть
        right = merge_sort(array[middle:])  # и правую
        return merge(left, right)  # выполняем слияние

def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort(array))
element = int(input("Введите число в диапазоне заданных чисел: "))

array.append(element)

print(merge_sort(array))

def binary_search(array, element):
    first = 0
    last = len(array)
    while first < last:
        middle = (first + last) // 2
        if element > array[middle]:
            first = middle + 1
        else:
            last = middle
    return first - 1 if 0 < first < len(array) else "Не входит в диапазон заданных чисел"

print("Индекс числа, которое меньше Вами введенного:", (binary_search(array, element)))