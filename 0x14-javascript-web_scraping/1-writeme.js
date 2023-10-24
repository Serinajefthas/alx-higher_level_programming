#!/usr/bin/node
// Script that writes string to file

const fs = require('fs');
if (process.argv.length !== 4) {
  console.error('Usage: node writeFile.js <file_path> <text_to_write>');
  process.exit(1);
}
fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err) {
  if (err) { return console.error(err); }
});
