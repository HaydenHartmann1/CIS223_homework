'''
Hayden Hartmann
Coding Problem: Quick Sort
6/19/2025
'''

def QuickSort(array):
    # If the len of the array is one or less then its already sorted
    if len(array) <= 1:
        return array
    # the pivot element within the array
    pivot = array[len(array) // 2]
    # Create empty arrays
    left = []
    middle = []
    right = []
    # Fill arrays with elements
    for x in array:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    # Recursive call
    return QuickSort(left) + middle + QuickSort(right)

test_run = [3, 6, 8, 10, 1, 2, 1]
print("Unsorted: ( ", end="")
for x in test_run:
    print(x, end=" ")
print(")")
sorted_test = QuickSort(test_run)
print("Sorted:   ( ", end="")
for x in sorted_test:
    print(x, end=" ")
print(")")
