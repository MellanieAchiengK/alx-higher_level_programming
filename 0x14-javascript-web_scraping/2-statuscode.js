#!/usr/bin/node
// display status code

const request = require('request');
const url = process.argv[2];

request(url, function (err, response) {
  if (err) {
    console.error(err);
  }
  console.log('code:', response && response.statusCode);
});
