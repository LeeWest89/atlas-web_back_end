// uniittest for api.js
const request = require('request');
const expect = require('chai').expect;

describe('Index Testing', () => {
  describe('GET /', () => {
    it('Welcome to the payment system', (done) => {
      const options = {
        url: 'http://localhost:7865',
        method: 'GET',
      };

      request(options, function (error, response) {
        expect(response.statusCode).to.equal(200);
        expect(response.body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });

  describe('GET /cart/12', () => {
    it('has correct code and id', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/12',
        method: 'GET',
      };
      request(options, function (error, response) {
        expect(response.statusCode).to.equal(200);
        expect(response.body).to.equal('Payment methods for cart 12');
        done();
      });
    });
  });

  describe('GET /cart/hello', () => {
    it('Has status 404', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/hello',
        method: 'GET',
      };
      request(options, function (error, response) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe('GET /cart/', () => {
    it('Has status 404', (done) => {
      const options = {
        url: 'http://localhost:7865/cart/',
        method: 'GET',
      };
      request(options, function (error, response) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });
});