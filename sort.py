class Sorting:
    """
    Класс для выполнения сортировок (быстрой и слиянием).

    `arr` - переменная, хранящая исходный неотсортированный массив.
    """
    def __init__(self, arr):
        self.arr = arr

    def do_quicksort(self):
        """
           Метод, вызывающий метод быстрой сортировки.
        """
        return self.quicksort(self.arr)

    def do_mergesort(self):
        """
            Метод, вызывающий метод сортировки слиянием.
        """
        return self.mergesort(self.arr)

    def quicksort(self, arr):
        """
            **Метод быстрой сортировки.**

            На вход подается неотсортированный массив `arr`.

            На выход - отсортированныый по возрастанию.


            **Алгоритм сортировки:**

            - Выбрать из массива элемент, называемый опорным - `pivot`.

            - Сравнить все остальные элементы с опорным и переставить их в массиве так, чтобы разбить массив на три непрерывных отрезка, следующих друг за другом: «элементы меньшие опорного» (`lesser`), «равные» и «большие» (`greater`).

            - Для отрезков «меньших» и «больших» значений выполнить рекурсивно ту же последовательность операций, если длина отрезка больше единицы.

            - Вернуть отсортированный по возрастанию массив.
        """
        lesser = []
        greater = []
        pivot = arr[0]
        for i in range(len(arr)):
            if arr[i] < pivot:
                lesser.append(arr[i])
            if arr[i] > pivot:
                greater.append(arr[i])
        if lesser:
            lesser = self.quicksort(lesser)
        if greater:
            greater = self.quicksort(greater)
        return lesser + [pivot] + greater

    def mergesort(self, arr):
        """
            **Метод сортировки слиянием.**

            На вход подается неотсортированный массив `arr`.

            На выход отсортированныый по возрастанию `sorted_arr`.


            **Алгоритм сортировки:**

            - Сортируемый массив разбивается на две части примерно одинакового размера (`left`, `right`).

            - Каждая из получившихся частей сортируется отдельно тем же алгоритмом.

            - Два упорядоченных массива половинного размера соединяются в один.

            - Возвращается отсортированный по возрастанию массив.
        """
        if len(arr) == 1 or len(arr) == 0:
            return arr
        left = self.mergesort(arr[:len(arr) // 2])
        right = self.mergesort(arr[(len(arr) // 2) + 1:])
        n = m = 0
        sorted_arr = []
        while n < len(left) and m < len(right):
            if left[n] <= right[m]:
                sorted_arr.append(left[n])
                n += 1
            else:
                sorted_arr.append(right[m])
                m += 1
        while n < len(left):
            sorted_arr.append(left[n])
            n += 1
        while m < len(right):
            sorted_arr.append(right[m])
            m += 1
        return sorted_arr


if __name__ == '__main__':
    a = Sorting([1, 2, -10, 787, 4, 21])
    print(a.do_mergesort())
    print(a.do_quicksort())
