export default function cleanSet(array, startString) {
  if (startString.length === 0) return '';

  const newString = [];
  for (const value of array) {
    if (value.includes(startString)) {
      newString.push(value.replace(startString, ''));
    }
  }

  return newString.join('-');
}
