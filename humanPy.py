#Bubble Sort
def bubbleSort(arr):
    #amount of times the loop will run
    for i in range(len(arr) - 1):
        #start at the beginning and check to the end
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr


print(bubbleSort([1, 2, 3, 4, 5]))
print(bubbleSort([5, 4, 3, 2, 1]))
print(bubbleSort([1, 2, 3, 5, 4]))
print(bubbleSort([5, 5, 5, 5, 5]))