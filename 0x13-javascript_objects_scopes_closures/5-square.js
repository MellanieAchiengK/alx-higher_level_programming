#!/usr/bin/node
// class Square that inherits from Rectangle

module.exports = class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
};
