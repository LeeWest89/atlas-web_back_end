/* eslint-enable no-unused-vars */
export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task = true;
    const task2 = false;
  }
  /* eslint-enable no-unused-vars */
  return [task, task2];
}
