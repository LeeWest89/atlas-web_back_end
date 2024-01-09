import handleProfileSignup from './6-final-user';

const queuePromise = handleProfileSignup('John', 'Doe', 'Gerald.jpg');

queuePromise.then((queue) => {
  console.log(queue);
}).catch((error) => {
  console.error('Error:', error);
});
