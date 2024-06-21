// test for 2-calcul.js
const expect = require('chai').expect
const calculateNumber = require('./1-calcul')

describe('calculateNumber', function() {
  // tests for SUM
  it('should return correct vaules for SUM', function() {
    expect(calculateNumber('SUM', 1, 3), 4);
    expect(calculateNumber('SUM', 1.5, 0), 2);
    expect(calculateNumber('SUM', 0.2, -0.3), 0);
    expect(calculateNumber('SUM', -5.43, -3.81), -9);
  });

  // tests for SUBTRACT
  it('should return correct vaules for SUBTRACT', function() {
    expect(calculateNumber('SUBTRACT', 1, 3), -2);
    expect(calculateNumber('SUBTRACT', 1.5, 0), 2);
    expect(calculateNumber('SUBTRACT', 0.2, -0.3), 0);
    expect(calculateNumber('SUBTRACT', -5.43, -3.81), -1);
  });

  // tests for DIVID
  it('should return correct vaules for DIVIDE', function() {
    expect(calculateNumber('DIVIDE', 4, 2), 2);
    expect(calculateNumber('DIVIDE', 1.5, 0), 'Error');
    expect(calculateNumber('DIVIDE', 5.5, 3.2), 2);
    expect(calculateNumber('DIVIDE', -8.43, -3.81), 2);
  });
});
