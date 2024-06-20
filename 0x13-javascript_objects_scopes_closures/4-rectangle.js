#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // If w or h is 0, negative, or not an integer, create an empty object
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    // check if width and height exist
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }

  rotate () {
    const swap = this.width;
    this.width = this.height;
    this.height = swap;
  }
}

module.exports = Rectangle;
