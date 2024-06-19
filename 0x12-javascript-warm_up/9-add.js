#!/usr/bin/node

const arg = process.argv.slice(2);

const a = parseInt(arg[0]);
const b = parseInt(arg[1]);

function add (a, b) {
  return a + b;
}

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}
