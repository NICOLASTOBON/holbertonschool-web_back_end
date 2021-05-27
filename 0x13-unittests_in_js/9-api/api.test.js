const { expect } = require('chai');
const request = require('request');

const URL = 'http://localhost:7865/'

describe('Index page => http://localhost:7865/', () => {
  it('[Correct status] 200', (done) => {
    request.get(URL, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done()
    })
  });
  it('[Correct result] Welcome to the payment system', (done) => {
    request.get(URL, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done()
    })
  });
})

describe('Cart page => http://localhost:7865/cart/:id', () => {
  it('[Correct status] 200', (done) => {
    request.get(URL + 'cart/12', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done()
    })
  });
  it('[Correct result] Payment methods for cart 12', (done) => {
    request.get(URL + 'cart/12', (error, response, body) => {
      expect(body).to.equal('Payment methods for cart 12');
      done()
    })
  });
  it('[Not found] status code 404', (done) => {
    request.get(URL + 'cart/hello', (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done()
    })
  })
})
