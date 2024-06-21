// test for 1-calcul.js
const assert = require('assert');
const calculateNumber = require('./1-calcul')

describe('calculateNumber', function() {
  // tests for SUM
  it('should return correct vaules for SUM', function() {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    assert.strictEqual(calculateNumber('SUM', 1.5, 0), 2);
    assert.strictEqual(calculateNumber('SUM', 0.2, -0.3), 0);
    assert.strictEqual(calculateNumber('SUM', -5.43, -3.81), -9);
  });

  // tests for SUBTRACT
  it('should return correct vaules for SUBTRACT', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3), -2);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 0), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', 0.2, -0.3), 0);
    assert.strictEqual(calculateNumber('SUBTRACT', -5.43, -3.81), -1);
  });

  // tests for DIVID
  it('should return correct vaules for DIVIDE', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 4, 2), 2);
    assert.strictEqual(calculateNumber('DIVIDE', 1.5, 0), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 5.5, 3.2), 2);
    assert.strictEqual(calculateNumber('DIVIDE', -8.43, -3.81), 2);
  });
});
