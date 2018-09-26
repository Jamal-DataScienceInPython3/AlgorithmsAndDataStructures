__author__ = "Jamal Muradov"
#!/usr/bin/env python3

def bubble_sort(arr, size):
    """This function sort the data by using bubble sort
    usage: bubble_sort(data, size_of_data)"""
    
    for i in range(size-1):
        for j in range(size-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j] #swap the values 

#Test
array = [1,2,4,3,6,9,8,7]
size = len(array)
bubble_sort(array, size)
print(array)
