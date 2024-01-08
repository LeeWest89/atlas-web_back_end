export default function cleanSet(set, startString) {
  if (startString === '') {
    return '';
  }
  const values = Array.from(set)
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length));
  return values.join('-');
}
