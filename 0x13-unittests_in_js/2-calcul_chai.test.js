const calculateNumber = require('./2-calcul_chai');
const { expect } = require('chai');

describe("calculateNumber - SUM", function () {
  it("should round (1.4) + (4.5) = 6", function () {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });
  it("should round (1.3) + (4.3) = 5", function () {
    expect(calculateNumber('SUM', 1.3, 4.3)).to.equal(5);
  });
  it("should round (-1.3) + (4.3) = 3", function () {
    expect(calculateNumber('SUM', -1.3, 4.3)).to.equal(3);
  });
  it("should round (1.3) + (-4.3) = -3", function () {
    expect(calculateNumber('SUM', 1.3, -4.3)).to.equal(-3);
  });
})

describe("calculateNumber - SUBTRACT", function () {
  it("should round (1.4) - (4.5) = -4", function () {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
  });
  it("should round (1.5) - (4.3) = -2", function () {
    expect(calculateNumber('SUBTRACT', 1.5, 4.3)).to.equal(-2);
  });
  it("should round (-1.3) - (4.3) = -5", function () {
    expect(calculateNumber('SUBTRACT', -1.3, 4.3)).to.equal(-5);
  });
  it("should round (1.3) - (-4.3) = 5", function () {
    expect(calculateNumber('SUBTRACT', 1.3, -4.3)).to.equal(5);
  });
})

describe("calculateNumber - DIVIDE", function () {
  it("should round a and b and return by the type", function () {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
  });
  it("should round a and b and return by the type", function () {
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  } )
})
