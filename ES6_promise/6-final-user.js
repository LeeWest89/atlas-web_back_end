import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const user = signUpUser(firstName, lastName).then((response) => ({
    status: 'fulfilled',
    value: response,
  }));

  const photo = uploadPhoto(fileName).catch((error) => ({
    status: 'rejected',
    value: error,
  }));

  return Promise.all([user, photo]);
}
