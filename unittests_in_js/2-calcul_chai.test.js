// test for 2-calcul.js
const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai')

describe('calculateNumber', function() {
  // tests for SUM
  describe('SUM test', function() {
    it('should return correct values for SUM', function() {
      expect(calculateNumber('SUM', 1, 3)).to.equal(4);
      expect(calculateNumber('SUM', 1.5, 0)).to.equal(2);
      expect(calculateNumber('SUM', 0.2, -0.3)).to.equal(0);
      expect(calculateNumber('SUM', -5.43, -3.81)).to.equal(-9);
    });
  });

  // tests for SUBTRACT
  describe('SUBTRACT test', function() {
    it('should return correct values for SUBTRACT', function() {
      expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
      expect(calculateNumber('SUBTRACT', 1.5, 0)).to.equal(2);
      expect(calculateNumber('SUBTRACT', 0.2, -0.3)).to.equal(0);
      expect(calculateNumber('SUBTRACT', -5.43, -3.81)).to.equal(-1);
    });
  });

  // tests for DIVID
  describe('DIVID test', function() {
    it('should return correct values for DIVIDE', function() {
      expect(calculateNumber('DIVIDE', 4, 2)).to.equal(2);
      expect(calculateNumber('DIVIDE', 1.5, 0)).to.equal('Error');
      expect(calculateNumber('DIVIDE', 5.5, 3.2)).to.equal(2);
      expect(calculateNumber('DIVIDE', -8.43, -3.81)).to.equal(2);
    });
  });
});
