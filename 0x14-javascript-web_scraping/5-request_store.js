#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2]; // First argument: URL
const filePath = process.argv[3]; // Second argument: File path

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
