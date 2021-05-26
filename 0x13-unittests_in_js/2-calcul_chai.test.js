const calculateNumber = require('./1-calcul');
const { expect } = require('chai');

describe("calculateNumber", function () {
  it("should round a and b and return by the type", function () {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });
  it("should round a and b and return by the type", function () {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
  });
  it("should round a and b and return by the type", function () {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
  });
  it("should round a and b and return by the type", function () {
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  } )
})
