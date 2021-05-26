const calculateNumber = require('./0-calcul');
const assert = require('assert');

describe("calculateNumber", function () {
  it("should round a and b and return the sum", function () {
    assert.deepStrictEqual(calculateNumber(1, 3.7), 5);
  });
  it("should round a and b and return the sum", function () {
    assert.deepStrictEqual(calculateNumber(1.2, 3.7), 5);
  });
  it("should round a and b and return the sum", function () {
    assert.deepStrictEqual(calculateNumber(1.5, 3.7), 6);
  });
  it("should round a and b and return the sum", function () {
    assert.deepStrictEqual(calculateNumber(1.4, 3.4), 4);
  } )
})
