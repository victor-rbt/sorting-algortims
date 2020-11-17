class BubleSort:

    def __init__(self):
        pass

    def run(self, array):
        """Algoritmo BubleSort"""
        elements = len(array)-1
        ordered = False
        while not ordered:
            ordered = True
            for i in range(elements):
                if array[i] > array[i+1]:
                    array[i], array[i+1] = array[i+1],array[i]
                    ordered = False

        return 'BubleSort'
