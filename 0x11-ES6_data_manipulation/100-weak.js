export const weakMap = new WeakMap();

export function queryAPI(endPoint) {
  const counter = weakMap.get(endPoint);

  if (counter === undefined) weakMap.set(endPoint, 1);
  else if (counter + 1 >= 5) throw new Error('Endpoint load is high');
  else weakMap.set(endPoint, counter + 1);
}
