#!/usr/bin/node
// Prints arguments that can be converted to integers

if (isNaN(parseInt(process.argv[2])) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
