export default function cleanSet(array, startString) {
  const newString = [];

  if (startString.length === 0) return '';

  for (const value of array) {
    if (value.includes(startString)) {
      newString.push(value.replace(startString, ''));
    }
  }

  return newString.join('-');
}
