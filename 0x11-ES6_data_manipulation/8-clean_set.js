export default function cleanSet(set, startString) {
  if (startString.length === 0) return '';

  const newString = [];
  for (const value of set) {
    if (value.startsWith(startString)) {
      newString.push(value.replace(startString, ''));
    }
  }

  return newString.join('-');
}
