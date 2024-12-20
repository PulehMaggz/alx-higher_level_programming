#!/usr/bin/node

// Retrieve arguments and exclude the first two elements
const args = process.argv.slice(2).map(Number);

// Check if there are less than two arguments
if (args.length <= 1) {
  console.log(0);
} else {
  // Sort the arguments in descending order and get the second largest
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
