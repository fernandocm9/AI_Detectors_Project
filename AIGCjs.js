//ChatGPT - prompt: write a bubble sort algorithm in javascript
function bubbleSort(arr) {
    let n = arr.length;
    let swapped;
    
    for (let i = 0; i < n - 1; i++) {
        swapped = false;
        
        for (let j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]; // Swap elements
                swapped = true;
            }
        }
        
        if (!swapped) break; // Stop if no swaps occurred (already sorted)
    }
}

// Example usage
let arr = [64, 34, 25, 12, 22, 11, 90];
bubbleSort(arr);
console.log("Sorted array:", arr);
