#!/usr/bin/node
// prints number of movies with character "Wedge Antilles"

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (JSON.parse(body).results) {
    let counter = 0;
    for (const movies of JSON.parse(body).results) {
      for (const character of movies.characters) {
        if (character.slice(-3, -1) === '18') {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
