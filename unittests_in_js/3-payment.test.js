// test for 3-payment.js
const sinon = require('sinon');
const assert = require('assert');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  it('should call Utils.calculateNumber', () => {
    const calSpy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);
    sinon.assert.calledOnce(calSpy);
    sinon.assert.calledOnceWithExactly(calSpy, 'SUM', 100, 20);
    calSpy.restore();
  });
});
