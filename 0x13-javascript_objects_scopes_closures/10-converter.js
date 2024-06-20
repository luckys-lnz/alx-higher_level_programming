#!/usr/bin/node

exports.converter = function (base) {
  const digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';

  return function convert (number) {
    if (number === 0) {
      return '0';
    }

    let result = '';

    while (number > 0) {
      result = digits[number % base] + result;
      number = Math.floor(number / base);
    }

    return result;
  };
};
