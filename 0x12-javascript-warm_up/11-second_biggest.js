#!/usr/bin/node
/* function secondLargest(array) {
  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (let num of array) {
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }
  return secondLargest;
} */
if (process.argv.length < 4) {
  console.log(0);
} else {
  const array = process.argv.slice(2).sort((a, b) => a - b).reverse();
  console.log(array[1]);
}
