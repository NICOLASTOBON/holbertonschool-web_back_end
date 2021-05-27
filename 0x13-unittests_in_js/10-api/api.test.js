const { expect } = require('chai');
const request = require('request');

const URL = 'http://localhost:7865/'

describe('GET /', () => {
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

describe('GET /cart/:id', () => {
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

describe('GET /available_payments', () => {
  it('[Correct status] 200', (done) => {
    request.get(URL + 'available_payments', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done()
    })
  });
  it('[Correct result] object', (done) => {
    request.get(URL + 'available_payments', (error, response, body) => {
      expect(JSON.parse(body)).to.eql({ payment_methods: { credit_cards: true, paypal: false } })
      done()
    })
  });
})

describe('POST /login', () => {
  it('[Correct status] 200', (done) => {
    const options = {
      json: { "userName": "Betty" }
    }
    request.post(URL + 'login', options, (err, httpResponse, body) => {
        expect(httpResponse.statusCode).to.equal(200);
        done()
    })
  });
  it('[Correct result] Welcome Betty', (done) => {
    const options = {
      json: { "userName": "Betty" }
    }
    request.post(URL + 'login', options, (err, httpResponse, body) => {
        expect(body).to.equal('Welcome Betty')
        done()
    })
  });
})
