const kue = require('kue');

const queue = kue.createQueue();

const sendNotification = (phoneNumber, message, done) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
};

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, done);
});
