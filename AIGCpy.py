#ChatGPT - prompt: write a bubble sort algorithm in python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                swapped = True
        if not swapped:  
            break  

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)


#Gemini - prompt: write a bubble sort algorithm in python
def bubble_sort(arr):
    """
    Sorts a list using the bubble sort algorithm.

    Args:
        arr: The list to be sorted.

    Returns:
        The sorted list.
    """
    n = len(arr)
    for i in range(n):
        # Flag to optimize, if no swaps occur, the list is sorted
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
                swapped = True
        # If no two elements were swapped in inner loop, the array is sorted
        if not swapped:
            break
    return arr

# Example usage:
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print("Sorted list:", sorted_list)

# Example usage 2
unsorted_list2 = [5, 1, 4, 2, 8]
sorted_list2 = bubble_sort(unsorted_list2)
print("Sorted list 2:", sorted_list2)



#Grok3 - prompt: write a bubble sort algorithm in python
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
if __name__ == "__main__":
    # Test the function with an example array
    array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", array)
    sorted_array = bubble_sort(array)
    print("Sorted array:", sorted_array)
    
    
    
#Claude - prompt: write a bubble sort algorithm in python
def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n - 1):
        # Flag to optimize if no swaps occur in a pass
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if current element is greater than next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred in this pass, array is sorted
        if not swapped:
            break
    
    return arr




#Perplexity - prompt: write a bubble sort algorithm in python
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Flag to optimize the algorithm
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return arr

# Example usage:
unsorted_array = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", unsorted_array)
sorted_array = bubble_sort(unsorted_array)
print("Sorted array:", sorted_array)
