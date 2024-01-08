export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }
  const int8A = new Int8Array(new ArrayBuffer(length));
  int8A.fill(0);
  int8A[position] = value;
  return new DataView(new ArrayBuffer(length));
}
