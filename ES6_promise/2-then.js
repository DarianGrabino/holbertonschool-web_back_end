export default function handleResponseFromAPI(promise) {
  promise
    .then((result) => {
      console.log(result);
      return {
        status: 200, body: 'success',
      };
    })
    .catch((error) => error)
    .finally(() => {
      console.log('Got a response from the API');
    });
}
