export default function hasValuesFromArray(array, numbers) {
  let numbersOfTrue = 0;

  numbers.forEach((number) => {
    const valueInSet = array.has(number);
    if (valueInSet) numbersOfTrue += 1;
  });

  return numbersOfTrue === numbers.length;
}
