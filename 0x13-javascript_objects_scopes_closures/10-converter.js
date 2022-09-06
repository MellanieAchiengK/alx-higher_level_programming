#!/usr/bin/node
// converst number from base 10 to another base passed as argument

exports.converter = function (base) {
  return num => num.toString(base);
};
