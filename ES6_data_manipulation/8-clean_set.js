export default function cleanSet(set, startString) {
  if (!startString.length || !startString) {
    return '';
  }
  const values = Array.from(set)
    .filter((value) => value && value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-');
  return values.length > 0 ? values : '';
}
