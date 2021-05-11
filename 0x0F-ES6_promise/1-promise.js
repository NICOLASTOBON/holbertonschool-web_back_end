function getFullResponseFromAPI(boolean) {
  return new Promise((res, rej) => {
    if (boolean) {
      res({ status: 200, body: 'Success' });
    } else {
      rej(new Error('The fake API is not working currently'));
    }
  });
}

export default getFullResponseFromAPI;
