const getPaymentTokenFromAPI = require('./6-payment_token');
const { expect } = require('chai');

describe('getPaymentTokenFromAPI', () => {
  it('Async tests with done', (done) => {
    getPaymentTokenFromAPI(true)
      .then((result) => {
        expect(result.data).to.equal('Successful response from the API');
        done()
      })
  })
})
