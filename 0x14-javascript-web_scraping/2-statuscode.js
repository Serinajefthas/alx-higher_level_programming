#!/usr/bin/node
// Script displays status code of get request

const request = require('request');

if (process.argv.length < 3) {
  console.error('Incorrect number of arguments');
  process.exit(1);
}
request(process.argv[2], function (error, response) {
  if (error) { console.error(error.message); } else { console.log('code: ${response.statusCode}'); }
});
