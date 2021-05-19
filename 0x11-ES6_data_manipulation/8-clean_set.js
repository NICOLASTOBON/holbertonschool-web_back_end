export default function cleanSet(array, startString) {
  const newString = [];

  for (const value of array) {
    if (value.includes(startString) && startString.length > 0) {
      newString.push(value.replace(startString, ''));
    }
  }
  return newString.join('-');
}
