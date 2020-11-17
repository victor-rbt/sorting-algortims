from algoritms.BubleSort import BubleSort
from algoritms.InsertionSort import InsertionSort
from algoritms.QuickSort import QuickSort

import random
import time

class Run:

    bublesort = BubleSort()
    insertionsort = InsertionSort()
    quicksort = QuickSort()
    
    def __init__(self):
        pass

    def initialize(self):
        """Inicializa os algoritmos"""
        array = []
        tam = input("Digite o tamanho da lista: ")

        for num in range(tam):
            array.append(random.randint(0, 9))

        instances = [self.bublesort, self.insertionsort, self.quicksort]

        for item in instances:
            new_array = array[:]
            begin = time.time()
            res = item.run(new_array)
            end = time.time()

            print("-"*50)
            print("Processamento do {algoritm} em {timer} ms.").format(algoritm=res, timer=((end-begin) * 1000))

instance = Run()
instance.initialize()
