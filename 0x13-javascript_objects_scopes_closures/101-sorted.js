#!/usr/bin/node
const dict = require('./101-data.js').dict;

const numsGr = Object.keys(dict).reduce((acc, k) => {
  const numGr = dict[k];
  acc[numGr] = acc[numGr] || [];
  acc[numGr].push(k);
  return acc;
}, {});

console.log(numsGr);
