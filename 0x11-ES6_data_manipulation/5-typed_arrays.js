function createInt8TypedArray(length, position, value) {
  try {
    const buffer = new ArrayBuffer(length);
    new DataView(buffer).setInt8(position, value);

    return buffer;
  } catch (e) {
    throw new Error('Position outside range');
  }
}

export default createInt8TypedArray;
