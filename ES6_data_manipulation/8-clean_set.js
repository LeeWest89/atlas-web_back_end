export default function cleanSet(set, startString) {
  if (startString.length === 0 || (typeof startString !== 'string' && typeof startString === 'object')) {
    return '';
  }
  let values = Array.from(set)
    .filter((value) => value && value.startsWith(startString))
    .map((value) => value.slice(startString.length));
  values = values || [];
  return values.length > 0 ? values.join('-') : '';
}
