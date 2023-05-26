import random
import threading
import time

class SortArray:
    def __init__(self):
        self.arr = []

    def fill_random(self):
        self.arr = [random.randint(1, 10000) for _ in range(10000)]

    def fill_manual(self):
        self.arr = [int(input(f"Enter value {i + 1}: ")) for i in range(10000)]

    def print_array(self):
        print(self.arr)

    def sort(self):
        pass

class SelectionSort(SortArray):
    def selection_sort(self):
        n = len(self.arr)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            if min_index != i:
                self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
        return self.arr

class InsertionSort(SortArray):
    @property
    def insertion_sort(self):
        n = len(self.arr)
        for i in range(1, n):
            current_value = self.arr[i]
            j = i - 1
            while j >= 0:
                if current_value < self.arr[j]:
                    self.arr[j + 1] = self.arr[j]
                    self.arr[j] = current_value
                    j = j - 1
                else:
                    break
        return self.arr


class QuickSort(SortArray):
    def quick_sort(self, arr=None):
        if arr is None:
            arr = self.arr
        n = len(arr)
        if n <= 1:
            return arr
        else:
            pivot = random.choice(arr)
            less = [x for x in arr if x < pivot]
            greater_or_equal = [x for x in arr if x >= pivot]
            return self.quick_sort(less) + self.quick_sort(greater_or_equal)

def sort_in_thread(sort_class):
    sort_object = sort_class()
    sort_object.fill_random()
    start_time = time.time()
    sorted_arr = sort_object.sort()
    print(f"{sort_class.__name__} sorted in {time.time() - start_time} seconds")
    print(sorted_arr)

def main():
    selection_sort_thread = threading.Thread(target=sort_in_thread, args=(SelectionSort,))
    insertion_sort_thread = threading.Thread(target=sort_in_thread, args=(InsertionSort,))
    quick_sort_thread = threading.Thread(target=sort_in_thread, args=(QuickSort,))

    selection_sort_thread.start()
    insertion_sort_thread.start()
    quick_sort_thread.start()

if __name__ == '__main__':
    main()