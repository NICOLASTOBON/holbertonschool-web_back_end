export default function updateUniqueItems(map) {
  if (!(map instanceof Object)) throw new Error('Cannot process');

  for (const [grocery, quantity] of map) {
    if (quantity === 1) map.set(grocery, 100);
  }
}
