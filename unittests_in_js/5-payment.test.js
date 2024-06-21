// test for 5-payment.js
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
  let conSpy;

  beforeEach(() => {
    conSpy = sinon.spy(console, 'log')
  });

  afterEach(() => {
    conSpy.restore();
  });

  it('should log "The total is: 120"', () => {
    sendPaymentRequestToApi(100, 20);
    sinon.assert.calledOnce(conSpy);
    sinon.assert.calledWithExactly(conSpy, 'The total is: 120');
  });

  it('should log "The total is: 20"', () => {
    sendPaymentRequestToApi(10, 10);
    sinon.assert.calledOnce(conSpy);
    sinon.assert.calledWithExactly(conSpy, 'The total is: 20');
  });
});
