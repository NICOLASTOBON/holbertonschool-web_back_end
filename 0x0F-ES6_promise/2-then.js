function handleResponseFromAPI(promise) {
  promise
    .then({ status: 200, body: 'Success' })
    .then(new Error())
    .then(console.log('Got a response from the API'));
}

export default handleResponseFromAPI;
