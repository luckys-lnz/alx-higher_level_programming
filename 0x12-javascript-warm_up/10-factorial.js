#!/usr/bin/node

const arg = process.argv[2];

const x = parseInt(arg);

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else if (n < 0) {
    return -1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(x));
