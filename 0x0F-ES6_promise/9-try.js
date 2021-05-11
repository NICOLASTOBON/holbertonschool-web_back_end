function guardrail(mathFunction) {
  const queue = [];
  const message = 'Guardrail was processed';

  try {
    const value = mathFunction();
    queue.push(value, message);
  } catch (err) {
    queue.push(`Error: ${err.message}`, message);
  }

  return queue;
}

export default guardrail;
