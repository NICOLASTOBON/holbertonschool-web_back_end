const redis = require('redis');

const subscriber = redis.createClient();

subscriber.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
subscriber.on('connect', () => console.log('Redis client connected to the server'));

const CHANNEL = 'holberton school channel';

subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe(CHANNEL);
    subscriber.quit();
  }
});

subscriber.subscribe(CHANNEL);
