#!/usr/bin/node

// Recursive function to calculate factorial
function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

// Parse the first argument as an integer
const num = parseInt(process.argv[2]);

// Compute and print the factorial
console.log(factorial(num));
