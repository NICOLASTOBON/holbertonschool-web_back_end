import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((values) => {
      for (const promise of values) {
        if (promise.status === 'rejected') {
          promise.value = `Error: ${promise.reason.message}`;
          delete promise.reason;
        }
      }
      return values;
    });
}

export default handleProfileSignup;
