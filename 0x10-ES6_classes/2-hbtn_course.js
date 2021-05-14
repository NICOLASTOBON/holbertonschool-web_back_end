/* eslint no-underscore-dangle: ["error", { "allow": ["_name", "_length", "_students"] }] */

export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw new TypeError('Name must be a string');
    if (typeof length !== 'number') throw new TypeError('Length must be a number');
    if (!Array.isArray(students)) throw new TypeError('Students must be an array of strings');
    this._name = name;
    this._length = length;
    this._students = students;
  }

  set name(newName) {
    if (typeof newName !== 'string') throw new TypeError('Name must be a string');
    this._name = newName;
  }

  get name() {
    return this._name;
  }

  set length(newLen) {
    if (typeof newLen !== 'number') throw new TypeError('Length must be a number');
    this._length = newLen;
  }

  get length() {
    return this._length;
  }

  set students(newStudents) {
    if (!Array.isArray(newStudents)) throw new TypeError('Students must be an array of strings');
    this._students = newStudents;
  }

  get students() {
    return this._students;
  }
}
