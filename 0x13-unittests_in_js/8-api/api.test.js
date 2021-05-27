const { expect } = require('chai');
const request = require('request');

const URL = 'http://localhost:7865'

describe('Index page', () => {
  it('Correct status code', (done) => {
    request.get(URL, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done()
    })
  });
  it('Correct result', (done) => {
    request.get(URL, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done()
    })
  })
})
