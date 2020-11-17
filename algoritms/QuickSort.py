import sys 
  
sys.setrecursionlimit(10**6)

class QuickSort:

    def __init__(self):
        pass

    def partition(self, array, start, end):
        pivot = array[start]
        low = start + 1
        high = end

        while True:
            while low <= high and array[high] >= pivot:
                high = high - 1

            while low <= high and array[low] <= pivot:
                low = low + 1

            if low <= high:
                array[low], array[high] = array[high], array[low]
            else:
                break

        array[start], array[high] = array[high], array[start]

        return high

    def run(self, array, start=None, end=None):
        if not start and not end:
            start = 0
            end = len(array) - 1
        if start >= end:
            return

        p = self.partition(array, start, end)
        self.run(array, start, p-1)
        self.run(array, p+1, end)

        return 'QuickSort'
