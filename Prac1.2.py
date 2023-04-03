#Data structure practical 1.2
#Puthon prigram for sorting integer array using selection sort

def selectionSort(array):
    n = len(array)
    for i on range(n-1):

        minimum = i

        for j in range(i+1, n):
            if (array[j] < array[minimum]):

        minimum = j

        array[i].array[minimum]