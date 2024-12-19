#!/usr/bin/node

// Get the arguments passed to the script
const args = process.argv;

// Check the number of arguments
if (args.length === 2) {
  console.log('No argument');
} else if (args.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
