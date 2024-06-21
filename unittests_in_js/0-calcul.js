// Function that takes two args(numbers) rounds and returns sum
function calculateNumber(a, b) {
  const sum = (Math.round(a) + Math.round(b));
  return (sum === 0 ? 0 : sum);
}

module.exports = calculateNumber;
