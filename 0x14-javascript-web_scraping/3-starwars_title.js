#!/usr/bin/node
// Script that prints the title of a Star Wars movie based on episode number

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the API
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
