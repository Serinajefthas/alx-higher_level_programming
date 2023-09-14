#!/usr/bin/node
let numArgs;
numArgs = process.argv.length;

if (numArgs === 2)
  console.log("No argument");
else if (numArgs === 3)
  console.log("Argument found");
else
  console.log("Arguments found");
