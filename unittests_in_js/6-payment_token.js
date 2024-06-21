// function that returns  a resolved promise with the object {data: 'Successful response from the API' } or nothing
function getPaymentTokenFromAPI(success) {
  if (success) {
    return Promise.resolve({ data: 'Successful response from the API' });
  } else {
    return Promise.resolve(null);
  }
}

module.exports = getPaymentTokenFromAPI;
