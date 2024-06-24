// Same as task 0, adding two functions
import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server')
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`)
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolname) {
  client.get(schoolname, (error, response) => {
    if (error) {
      console.error(`${schoolname}: ${error.message}`);
    } else {
    console.log(response);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
