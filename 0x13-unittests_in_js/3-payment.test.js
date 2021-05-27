const { expect } = require('chai');
const sinon = require('sinon');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function() {
  it('validate the usage of the Utils function', function() {
    const callSpy = sinon.spy(Utils, 'calculateNumber');
    const apiResponse = sendPaymentRequestToApi(100, 2);
    
    expect(callSpy.calledOnce).to.be.true;
    expect(Utils.calculateNumber('SUM', 100, 2)).to.equal(apiResponse);

    callSpy.restore();
  })
})
