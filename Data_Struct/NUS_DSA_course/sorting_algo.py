import math
import random
import time

"""
Adapted for DS&A Short Course - by SYJ
Version 2.2 (2022 June)

For IT5003 - by SYJ 

Version 2.1 (2020 February)
- Added timing code

Version 2.0 (2020 February)
- Updated insertionSort()

Version 1.0 (2019 September)
- Implemented all sorting algorithms covered
- Basic documentation for each sorting function

"""

def swapElement(array, x, y):
    """
    swap array[x] with array[y]
    """
    #print("swap {:d} with {:d}".format(x, y))
    temp = array[x]
    array[x] = array[y]
    array[y] = temp

def selectionSort(array):
    """
    Selection sort on array
    """
    n = len(array)
    for i in range(n-1,0, -1):
        #print(i)
        maxIdx = i
        for j in range(0, i):
            if array[j] > array[maxIdx]:
                maxIdx = j
        swapElement(array, maxIdx, i)

def insertionSort(array):
    """
    Insertion sort on array
    """
    n = len(array)
    for i in range (1, n):
        next = array[i]
        j = i-1
        while j >= 0 and array[j] > next:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = next

def bubbleSort(array):
    """
    Standard bubble sort on array
    """
    n = len(array)
    for i in range(n-1, 0, -1):
        for j in range (1, i+1):
            if array[j-1] > array[j]:
                swapElement(array, j, j-1) 

def bubbleSortEarly(array):
    """
    Bubble sort with early termination
    """
    n = len(array)
    for i in range(n-1, 0, -1):
        isSorted = True
        for j in range (1, i+1):
            if array[j-1] > array[j]:
                swapElement(array, j, j-1) 
                isSorted = False
        if isSorted:
            return


def mergeSort( array, low, high ):
    """
    Merge sort items array[low...high]
    """
    if low < high:
        mid = (low+high) // 2

        mergeSort(array, low, mid)
        mergeSort(array, mid+1, high)
        merge(array, low, mid, high)

def merge( array, low, mid, high ):
    """
    Merge two sorted subarray: array[low...mid] with array[mid+1...high]
    """
    n = high-low+1
    result = []
    left = low
    right = mid+1
    #print("Merge [{:d}-{:d}] with [{:d}-{:d}]".format(low, mid, right, high))


    while left <= mid and right <= high:
        if array[left] <= array[right]:
           result.append(array[left])
           left = left + 1
        else:
            result.append(array[right])
            right = right + 1

    while left <= mid:
        result.append(array[left])
        left = left + 1

    while right <= high:
        result.append(array[right])
        right = right + 1

    for k in range(0, n):
        array[low+k] = result[k]

def mergeSortHelper(array):
    """
    Merge sort wrapper so that this function takes in the same parameter with
    all other sorting functions.
    """
    mergeSort(array, 0, len(array)-1)

def quickSort ( array, low, high ):
    """
    Quick sort on array[low..high]
    """
    if low < high :
        pivotIdx = partition( array, low, high )
        quickSort( array, low, pivotIdx-1)
        quickSort( array, pivotIdx + 1, high )

def partition( array, i, j ):
    """
    Partition function: User array[i] to partition array[i+1...j] into two subarrays. 
    Left array <= array[i], right array > array[i]
    Return index of array[i] after placing it at the end of left array
     """
    pivot = array[i]
    middle = i

    for k in range (i+1,j+1):
        if array[k] < pivot:
            middle = middle + 1
            swapElement(array, k, middle)

    swapElement(array, i, middle)
    return middle

def quickSortHelper(array):
    """
    Quick sort wrapper so that this function takes in the same parameter with
    all other sorting functions.
    """
    quickSort(array, 0, len(array)-1)

def radixSort(array):
    """
    Radix sort on array
    """
    numDigit = int(math.log10(max(array))) + 1
    #print("Number of Digit = {:d}".format(numDigit))
    for power in [10**i for i in range(numDigit)]:
        digitBin = [[] for d in range(10)]
        distribute(array, digitBin, power)
        collect(digitBin, array)

def distribute(array, digitBin, power):
    """
    Distribute number in array into 10 subarrays based on the digit at power position.
    """
    for item in array:
        digit = (item // power ) % 10
        digitBin[digit].append( item )
    #print("Distribute [Power = {:d}]".format(power))
    #print(list(enumerate(digitBin,0)))

def collect(digitBin, array):
    """
    Collect number in from 10 subarrays into a single array.
    """
    startIdx = 0
    for eachBin in digitBin:
        array[startIdx:] = eachBin
        startIdx += len(eachBin)
    #print("Collect")
    #print(array)

def main():

    #uncomment one of the following to test a specific sorting algorithm
    # sort = selectionSort
    sort = insertionSort
    #sort = bubbleSort
    #sort = bubbleSortEarly
    #sort = mergeSortHelper
    #sort = quickSortHelper
    #sort = radixSort

    #################################
    # Small Sorting Demo            #
    #################################

    #A few sample array with different characteristics
    # array1 = [2, 3, 5, 7, 11, 13, 17]    #already sorted
    # array2 = [17, 13, 11, 7, 5, 3, 2]    #reversely sorted
    # array3 = [11, 2, 5, 7, 3, 17, 13]    #only one item out of place
    # array4 = [11, 2, 11, 2, 11, 2]       #interleaved items
    # array5 = [123, 2154, 222, 4, 283, 1560, 1061, 2150] #item with multiple digits, for radix sort demo

    #uncomment one or more sorting examples below
    #sort(array1)
    #print(array1)

    # sort(array2)
    # print(array2)

    # sort(array3)
    # print(array3)

    # sort(array4)
    # print(array4)

    # sort(array5)
    # print(array5)

    #################################
    # Timing Demo                   #
    #################################
    
    #For user chosen array size and randomly generated array
    # N = int(input("Enter N: "))
    # bigArray = [random.randint(1, 1000000) for i in range(N)]

    # # Uncomment for time measurement
    # start_time = time.time()
    # sort(bigArray)
    # print("---Sort(%d) =  %s seconds ---" % (N, (time.time() - start_time)))
    
    #################################
    # Tutorial                      #
    #################################
    
    lis = [1285,5,150,4746,602,5,8356]
    # selectionSort(lis)
    sort(lis)


if __name__ == "__main__":
    main()

