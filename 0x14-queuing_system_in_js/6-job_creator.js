const kue = require('kue');

const queue = kue.createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '311-782-1915',
  message: 'Hello people',
});

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
job.save(() => console.log(`Notification job created: ${job.id}`));
