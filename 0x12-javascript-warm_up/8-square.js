#!/usr/bin/node

const arg = process.argv[2];
const x = parseInt(arg);

if (isNaN(x)) {
  console.log('Missing size');
}
for (let i = 0; i < x; i++) {
  console.log('x'.repeat(x));
}
