// function that takes 2 args and calls calculatNUmber from utlis.js
const Utlis = require('./utils')

function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const sum = Utlis.calculateNumber('SUM', totalAmount, totalShipping)
  console.log(`The total is: ${sum}`)
}

module.exports = sendPaymentRequestToApi;
