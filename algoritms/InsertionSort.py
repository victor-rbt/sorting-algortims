from random import randint
import time

class InsertionSort:

    def __init__(self):
        pass

    def run(self, array):
        """Algoritmo InsertionSort"""
        for index in range(0, len(array)):
            keys = array[index]
            k = index
            while k > 0 and keys < array[k - 1]:
                array[k] = array[k - 1]
                k -= 1
            array[k] = keys

        return 'InsertionSort'
