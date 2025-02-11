#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Get movie ID from command-line argument
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`; // API endpoint for the movie

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }
      console.log(JSON.parse(charBody).name);
    });
  });
});
