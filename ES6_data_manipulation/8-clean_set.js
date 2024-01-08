export default function cleanSet(set, startString) {
  if (startString.length === 0 || typeof startString !== 'string') {
    return '';
  }
  const values = Array.from(set)
    .filter((value) => value && value.startsWith(startString))
    .map((value) => value.slice(startString.length));
  return values.length > 0 ? values.join('-') : '';
}
