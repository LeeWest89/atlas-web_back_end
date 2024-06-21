// test for 4-payment.js
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
  it('should call Utils.calculateNumber', () => {
    const calStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    const conSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledOnce(calStub);
    sinon.assert.calledWithExactly(calStub, 'SUM', 100, 20);
    sinon.assert.calledOnce(conSpy);
    sinon.assert.calledWithExactly(conSpy, 'The total is: 10');

    calStub.restore();
    conSpy.restore();
  });
});
