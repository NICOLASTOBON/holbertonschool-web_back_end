/* eslint no-underscore-dangle: ["error", { "allow": ["_size", "_location"] }] */

export default class HolbertonClass {
  constructor(size, location) {
    if (typeof location !== 'string') throw new TypeError('Location must be a string');
    if (typeof size !== 'number') throw new TypeError('Size must be a number');

    this._size = size;
    this._location = location;
  }

  [Symbol.toPrimitive](hint) {
    if (hint === 'number') return this._size;
    if (hint === 'string') return this._location;
    return null;
  }
}
