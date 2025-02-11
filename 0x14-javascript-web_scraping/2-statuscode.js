#!/usr/bin/node
// Script that displays the status code of a GET request

const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

// Make a GET request to the provided URL
request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
