#!/usr/bin/node
// bases
exports.converter = function (base) {
  return function (toBase) {
    return toBase.toString(base);
  };
};
