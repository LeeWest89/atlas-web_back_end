export default function hasValuesFromArray(set, array) {
  return array.every((arr) => set.has(arr));
}
