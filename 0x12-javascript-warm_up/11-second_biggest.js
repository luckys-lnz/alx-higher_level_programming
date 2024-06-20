#!/usr/bin/node

const arg = process.argv.slice(2).map(Number);

function secondBiggest (n) {
  if (n.length <= 1) {
    return 0;
  }
  n.sort((a, b) => b - a);
  return n[1];
}
console.log(secondBiggest(arg));
