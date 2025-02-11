#!/usr/bin/node
// Script that writes a string to a file

const fs = require('fs');

// Get file path and string from command-line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the content to the file in UTF-8
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
