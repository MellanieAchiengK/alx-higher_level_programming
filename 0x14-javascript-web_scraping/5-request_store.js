#!/usr/bin/node
// gets webpage content and stores in a file

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, body, 'utf-8', function (err) {
      if (err) { console.log(err); }
    });
  }
});
