const { expect } = require('chai');
const sinon = require('sinon');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function() {
  it('validate the usage of the Utils function', function() {
    const consoleSpy = sinon.spy(console, 'log');
    const validateUtilFunc = sinon.stub(Utils, 'calculateNumber').returns(10);
    sendPaymentRequestToApi(100, 20);
    
    expect(validateUtilFunc.calledWith('SUM', 100, 20)).to.be.true;
    expect(consoleSpy.calledOnceWith('The total is: 10'))

    consoleSpy.restore();
    validateUtilFunc.restore();
  })
})
