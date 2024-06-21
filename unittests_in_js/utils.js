// utils

const Utils = {
  calculateNumber(type, a, b) {
    const roundA = Math.round(a);
    const roundB = Math.round(b);
  
    if (type === 'SUM') {
      const sum = (roundA + roundB);
  
      return (sum === 0 ? 0 : sum);
    }
  
    if (type === 'SUBTRACT') {
      const sub = (roundA - roundB);
  
      return (sub === 0 ? 0 : sub);
    }
  
    if (type === 'DIVIDE') {
  
      if (roundB === 0) {
        return ('Error')
      }
  
      const div = (roundA / roundB);
  
      return (div);
    }
  }
}

  module.exports = Utils;
