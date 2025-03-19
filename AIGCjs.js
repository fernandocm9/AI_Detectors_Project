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


//Gemini - prompt: write a bubble sort algorithm in javascript
function bubbleSort(arr) {
  const n = arr.length;
  let swapped;

  do {
    swapped = false;
    for (let i = 0; i < n - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        // Swap arr[i] and arr[i + 1]
        [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]]; // Destructuring assignment for swap
        swapped = true;
      }
    }
  } while (swapped);

  return arr;
}

// Example usage:
const unsortedArray = [64, 34, 25, 12, 22, 11, 90];
const sortedArray = bubbleSort(unsortedArray);
console.log("Sorted array:", sortedArray); // Output: Sorted array: [11, 12, 22, 25, 34, 64, 90]

// Another implementation with a small optimization.
function bubbleSortOptimized(arr){
  let n = arr.length;
  let swapped;
  for(let i=0; i < n-1; i++){
    swapped = false;
    for(let j=0; j < n-i-1; j++){
      if(arr[j] > arr[j+1]){
        [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
        swapped = true;
      }
    }
    if(swapped === false) break;
  }
  return arr;
}

const unsortedArray2 = [64, 34, 25, 12, 22, 11, 90];
const sortedArray2 = bubbleSortOptimized(unsortedArray2);
console.log("Sorted array optimized:", sortedArray2);



//Grok - prompt: write a bubble sort algorithm in javascript
function bubbleSort(arr) {
    let n = arr.length;
    let swapped;
    
    // Outer loop for number of passes
    for (let i = 0; i < n - 1; i++) {
        swapped = false;
        
        // Inner loop for comparing adjacent elements
        for (let j = 0; j < n - i - 1; j++) {
            // Compare adjacent elements
            if (arr[j] > arr[j + 1]) {
                // Swap if they are in wrong order
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
                swapped = true;
            }
        }
        
        // If no swapping occurred in this pass, array is already sorted
        if (!swapped) {
            break;
        }
    }
    
    return arr;
}

// Example usage:
let array = [64, 34, 25, 12, 22, 11, 90];
console.log("Original array:", array);
bubbleSort(array);
console.log("Sorted array:", array);



//Calude - prompt: write a bubble sort algorithm in javascript
function bubbleSort(arr) {
  const n = arr.length;
  
  for (let i = 0; i < n - 1; i++) {
    let swapped = false;
    
    // Last i elements are already in place
    for (let j = 0; j < n - i - 1; j++) {
      // Compare adjacent elements
      if (arr[j] > arr[j + 1]) {
        // Swap them if they are in wrong order
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        swapped = true;
      }
    }
    
    // If no swapping occurred in this pass, array is sorted
    if (!swapped) break;
  }
  
  return arr;
}



//Perplexity - prompt: write a bubble sort algorithm in javascript
function bubbleSort(arr) {
  const n = arr.length;
  let swapped;

  for (let i = 0; i < n - 1; i++) {
    swapped = false;

    for (let j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        // Swap elements
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        swapped = true;
      }
    }

    // If no swapping occurred, array is already sorted
    if (!swapped) break;
  }

  return arr;
}

// Example usage:
// const unsortedArray = [64, 34, 25, 12, 22, 11, 90];
// console.log("Unsorted array:", unsortedArray);
// const sortedArray = bubbleSort(unsortedArray);
// console.log("Sorted array:", sortedArray);
