#----------------------------------------------- insertion sort  
import copy
def insertion_sort(A):
    # Create a copy of the original list to avoid modifying the input
    sorted_list = A.copy()

    # Start sorting from the second element
    for j in range(1, len(sorted_list)):
        key = sorted_list[j]
        i = j - 1
        
        # Shift elements of the sorted part to the right to make space for the key
        while i >= 0 and sorted_list[i] > key:
            sorted_list[i + 1] = sorted_list[i]
            i -= 1
        
        # Insert the key at its correct position
        sorted_list[i + 1] = key

    return sorted_list

# ----------------------------------------------- recursive insersion sort

def recursive_insertion_sort(arr, n):
    if n <= 1:
        return arr.copy()  # Return a copy of the array to avoid motif original

    arr_copy = recursive_insertion_sort(arr, n-1)

    # Insert the last element at its correct position
    last = arr[n-1]
    j = n-2

    arr_copy.append(last)
    while j >= 0 and arr_copy[j] > last:
        arr_copy[j + 1] = arr_copy[j]
        j -= 1

    arr_copy[j + 1] = last

    return arr_copy
  

            