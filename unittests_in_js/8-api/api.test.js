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
});