// Same as task 1, making displaySchoolValue async
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getA = promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolname) {
  try {
    console.log(await getA(schoolname));
  } catch (error) {
    console.error(`${schoolname}: ${error.message}`);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
