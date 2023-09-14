#!/usr/bin/node
let arg;
arg = process.argv[2];

if (arg === undefined)
  console.log("No argument");
else
	console.log(arg);
