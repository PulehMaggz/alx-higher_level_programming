#!/usr/bin/node

// Get the first argument passed to the script
const arg = process.argv[2];

// Attempt to convert the argument to an integer
const num = parseInt(arg);

// Check if the conversion is successful (a valid number)
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
