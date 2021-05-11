import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((value) => ({ status: 'fulfilled', value }))
    .catch((err) => ({ status: 'rejected', value: `${err.name}: ${err.message}` }));
}

export default handleProfileSignup;
