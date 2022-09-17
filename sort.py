class Sorting:
    """
    Класс для выполнения сортировок (быстрой и слиянием).

    `list` - переменная, хранящая исходный неотсортированный список.
    """
    def __init__(self, list):
        self.list = list

    def do_quicksort(self):
        """
           Метод, вызывающий метод быстрой сортировки.

           На вход ничего не подаётся.

           Возвращает отсортированный по возрастанию список.
        """
        return self.quicksort(self.list)

    def do_mergesort(self):
        """
            Метод, вызывающий метод сортировки слиянием.

            На вход ничего не подаётся.

            Возвращает отсортированный по возрастанию список.
        """
        return self.mergesort(self.list)

    def quicksort(self, list):
        """
            **Метод быстрой сортировки.**

            На вход подается неотсортированный список `list`.

            На выход - отсортированный по возрастанию.


            **Алгоритм сортировки:**

            - Выбрать из списка элемент, называемый опорным - `pivot`.

            - Сравнить все остальные элементы с опорным и переставить их в списке так, чтобы разбить список на три непрерывных отрезка, следующих друг за другом: «элементы меньшие опорного» (`lesser`), «равные» и «большие» (`greater`).

            - Для отрезков «меньших» и «больших» значений выполнить рекурсивно ту же последовательность операций, если длина отрезка больше единицы.

            - Вернуть отсортированный по возрастанию список.
        """
        lesser = []
        greater = []
        pivot = list[0]
        for i in range(len(list)):
            if list[i] < pivot:
                lesser.append(list[i])
            if list[i] > pivot:
                greater.append(list[i])
        if lesser:
            lesser = self.quicksort(lesser)
        if greater:
            greater = self.quicksort(greater)
        return lesser + [pivot] + greater

    def mergesort(self, list):
        """
            **Метод сортировки слиянием.**

            На вход подается неотсортированный список `list`.

            На выход - отсортированный по возрастанию `sorted_list`.


            **Алгоритм сортировки:**

            - Сортируемый список разбивается на две части примерно одинакового размера (`left`, `right`).

            - Каждая из получившихся частей сортируется отдельно тем же алгоритмом.

            - Два упорядоченных списка половинного размера соединяются в один.

            - Возвращается отсортированный по возрастанию список.
        """
        if len(list) == 1 or len(list) == 0:
            return list
        left = self.mergesort(list[:len(list) // 2])
        right = self.mergesort(list[(len(list) // 2) + 1:])
        n = m = 0
        sorted_list = []
        while n < len(left) and m < len(right):
            if left[n] <= right[m]:
                sorted_list.append(left[n])
                n += 1
            else:
                sorted_list.append(right[m])
                m += 1
        while n < len(left):
            sorted_list.append(left[n])
            n += 1
        while m < len(right):
            sorted_list.append(right[m])
            m += 1
        return sorted_list


if __name__ == '__main__':
    list = [1, 2, -10, 787, 4, 21]
    a = Sorting(list)
    print(a.do_mergesort())
    print(a.do_quicksort())
