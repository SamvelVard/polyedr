def heapsort(list):
    n = len(list)

    # Функция для преобразования подмассива в кучу
    def heapify(list, n, i):

        largest = i  # Инициализируем наибольший элемент как корень
        left = 2 * i + 1  # Левый дочерний элемент
        right = 2 * i + 2  # Правый дочерний элемент

        # Если левый дочерний элемент больше корня
        if left < n and list[left] > list[largest]:
            largest = left

        # Если правый дочерний элемент больше, чем наибольший элемент
        if right < n and list[right] > list[largest]:
            largest = right

        # Если наибольший элемент не корень
        if largest != i:
            list[i], list[largest] = list[largest], list[i]  # Меняем местами
            heapify(list, n, largest)


    # Построение кучи (перегруппировка массива)
    for i in range(n // 2 - 1, -1, -1):
        heapify(list, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]  # Меняем местами
        heapify(list, i, 0)
    print(list)

# Пример использования
list_to_sort = [2, -1, 0, 7, 5, 1, 3, 2, 8, 6]
heapsort(list_to_sort)
print("Отсортированный массив:", list_to_sort)