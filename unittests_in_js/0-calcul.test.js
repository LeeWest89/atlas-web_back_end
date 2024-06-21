// test for 0-calcul.js
const assert = require('assert');
const calculateNumber = require('./0-calcul')

describe('calculateNumber', function() {
  // test for whole numbers
  it('should return 4 when inputs are 1 and 3', function() {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  // test for whole number and decimal number
  it('should return 5 when inputs are 1 and 3.7', function() {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  // test for 2 decimal number(One rounding down, one rounding up)
  it('should return 5 when inputs are 1.2 and 3.7', function() {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  // test for 2 decimal number(both rounding up)
  it('should return 6 when inputs are 1.5 and 3.7', function() {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  // test for 0 edge case
  it('should handle 0', function() {
    assert.strictEqual(calculateNumber(0, 0), 0);
    assert.strictEqual(calculateNumber(1, 0), 1);
    assert.strictEqual(calculateNumber(-1, 0), -1);
    assert.strictEqual(calculateNumber(0.2, 0.3), 0);
  });

  // test for negative edge case
  it('should handle 0', function() {
    assert.strictEqual(calculateNumber(-1, -2), -3);
    assert.strictEqual(calculateNumber(-1.4, -5.7), -7);
    assert.strictEqual(calculateNumber(-1, 0), -1);
    assert.strictEqual(calculateNumber(-0.2, -0.3), 0);
  });

  // test for mor than one decimal place
  it ('should calculate correctly', function() {
    assert.strictEqual(calculateNumber(1.22, 2.45), 3);
    assert.strictEqual(calculateNumber(1.45, 1.4999), 2);
    assert.strictEqual(calculateNumber(-1.39, -2.11111), -3);
  });
});
