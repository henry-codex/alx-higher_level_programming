#!/usr/bin/node
// Concat files
const fs = require('fs');
const data1 = fs.readFileSync(process.argv[2],
  { encoding: 'utf8', flag: 'r' });

const data2 = fs.readFileSync(process.argv[3],
  { encoding: 'utf8', flag: 'r' });

const concate = data1 + data2;

fs.writeFileSync(process.argv[4], concate);
