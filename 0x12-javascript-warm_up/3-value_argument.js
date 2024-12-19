#!/usr/bin/node

// Get the first argument passed to the script
const firstArg = process.argv[2];

// Check if an argument is provided
if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
