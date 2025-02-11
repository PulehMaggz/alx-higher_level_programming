#!/usr/bin/env node

const request = require('request');

// Check if URL is provided as an argument
if (process.argv.length < 3) {
  console.log('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

// The URL of the Star Wars API passed as an argument
const apiUrl = process.argv[2];

// The character ID for Wedge Antilles
const wedgeAntillesId = 18;

// Make a request to the API URL
request(apiUrl, (err, res, body) => {
  if (err) {
    console.log('Error:', err);
    return;
  }

  // Parse the response body to JSON
  const films = JSON.parse(body).results;

  // Initialize the counter for the number of films with Wedge Antilles
  let count = 0;

  // Loop through the films and check if Wedge Antilles is in the list of characters
  films.forEach((film) => {
    if (film.characters.some(characterUrl => characterUrl.includes(`/${wedgeAntillesId}/`))) {
      count++;
    }
  });

  // Print the result
  console.log(count);
});
