#!/usr/bin/node

// Get the first argument passed to the script
const size = parseInt(process.argv[2]);

// Check if the argument is a valid integer
if (isNaN(size) || size <= 0) {
  console.log('Missing size');
} else {
  // Use a loop to print the square
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
