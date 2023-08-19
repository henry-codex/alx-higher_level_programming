#!/usr/bin/node
// Reverse
exports.esrever = function (list) {
  const maxInd = list.length - 1;
  const list1 = [];
  for (let i = maxInd; i >= 0; i--) {
    list1.push(list[i]);
  }
  return (list1);
};
