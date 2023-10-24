#!/usr/bin/node
// Script reads and prints contents of file

const fs = require('fs');
if (process.argv.length < 3) {
  console.error('Usage: node readFile.js <file_path>');
  process.exit(1);
}
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) { return console.error(err); } else { console.log(data); }
});
