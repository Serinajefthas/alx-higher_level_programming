#!/usr/bin/node
function add (num1, num2) {
  console.log(parseInt(num1) + parseInt(num2));
}

if (process.argv.length !== 4) {
  console.log('NaN');
} else {
  add(process.argv[2], process.argv[3]);
}
