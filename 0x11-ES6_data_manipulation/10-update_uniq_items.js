export default function updateUniqueItems(map) {
  for (const [grocery, quantity] of map) {
    if (quantity === 1) map.set(grocery, 100);
  }
}
