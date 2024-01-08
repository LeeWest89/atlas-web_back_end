export default function cleanSet(set, startString) {
  if (!startString || !startString.length) {
    return '';
  }
  const values = Array.from(set)
    .filter((value) => value && value.startsWith(startString))
    .map((value, idx) => `${idx === 0 ? '' : '-'}${value.slice(startString.length)}`)
    .join('');
  return values.length > 0 ? values : '';
}
