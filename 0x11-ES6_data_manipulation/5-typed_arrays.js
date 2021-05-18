function createInt8TypedArray(length, position, value) {
  try {
    const buffer = new ArrayBuffer(length);
    const dataView = new DataView(buffer);

    dataView.setInt8(position, value);

    return dataView;
  } catch (e) {
    throw new Error('Position outside range');
  }
}

export default createInt8TypedArray;
