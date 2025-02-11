#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  // Function to fetch characters in order
  function fetchCharacter(index) {
    if (index >= characters.length) return;

    request(characters[index], (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }

      console.log(JSON.parse(charBody).name);
      fetchCharacter(index + 1); // Recursive call to maintain order
    });
  }

  fetchCharacter(0);
});
