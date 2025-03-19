//Bubble Sort
function bubbleSort(arr){
    for(let i = 0; i < arr.length - 1; i++){
        for(let j = 0; j < arr.length - 1 - i; j++){
            if(arr[j] > arr[j + 1]){
                let temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            }
        }
    }
    return arr
}

console.log(bubbleSort([1, 2, 3, 4, 5]))
console.log(bubbleSort([5, 4, 3, 2, 1]))
console.log(bubbleSort([1, 2, 3, 5, 4]))
console.log(bubbleSort([5, 5, 5, 5, 5]))
