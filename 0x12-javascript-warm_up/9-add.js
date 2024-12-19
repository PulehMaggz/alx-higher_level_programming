#!/usr/bin/node

// Function to add two numbers
function add (a, b) {
  return a + b;
}

// Parse the first and second arguments as integers
const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);

// Print the result of the addition
console.log(add(first, second));
