// connect to the Redis server running on your machine
import redis from 'redis';

redis.createClient().on('connect', () => {
  console.log('Redis client connected to the server');
});

redis.createClient().on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});
