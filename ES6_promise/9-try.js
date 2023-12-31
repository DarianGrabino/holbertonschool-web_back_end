export default function guardrail(mathFunction) {
  const queue = [];
  let result = '';
  try {
    result = mathFunction();
  } catch (error) {
    queue.push(String(error));
  }

  if (result) queue.push(result);
  queue.push('Guardrail was processed');
  return queue;
}
