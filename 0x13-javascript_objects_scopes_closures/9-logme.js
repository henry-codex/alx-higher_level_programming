#!/usr/bin/node
// print
let counter = 0;
exports.logMe = function (item) {
  console.log(`${counter}: ${item}`);
  counter++;
};
