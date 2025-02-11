#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // Get API URL from command line arguments

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const films = JSON.parse(body).results; // Parse JSON response and get the 'results' array
    const count = films.filter(movie =>
      movie.characters.some(character => character.includes('/18/'))
    ).length;

    console.log(count);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
