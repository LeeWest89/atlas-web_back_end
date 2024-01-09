export default function guardrail(mathFunction) {
  const queue = [];
  let result = 0;

  try {
    result = mathFunction();
  } catch (error) {
    result = `${error.name}: ${error.message}`;
  } finally {
    queue.push(result);
    queue.push('Guardrail was processed');
  }
  return queue;
}
