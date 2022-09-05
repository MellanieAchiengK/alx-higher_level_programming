#!/usr/bin/node
// computes and prints a factorial

function factorial (num) {
  if (isNaN(num) || num <= 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(Number(process.argv[2])));
