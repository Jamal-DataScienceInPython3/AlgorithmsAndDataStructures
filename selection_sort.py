__author__ = "Jamal Muradov"
#!/usr/bin/env python3

def selection_sort(arr, size):
    """This function sorts data by using selection sort algorithm.
Time complexity: O(n^2)
Usage: selection_sort(data, size_of_data)"""
    for i in range(size):
        _min = i
        for j in range(i,size):
            if arr[j]<arr[_min]:
                _min = j
        arr[_min], arr[i] = arr[i], arr[_min]
#Test
arr = [2,5,4,3,1,6,9,8,7]
print("\n=========Unsorted Array========", arr, sep="\n")
size = len(arr)
selection_sort(arr, size)
print("\n=========Sorted Array =========", arr, sep="\n")

