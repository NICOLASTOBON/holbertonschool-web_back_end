/* eslint-disable */

const queue = require('kue').createQueue();
const { afterEach } = require('mocha');
const { expect } = require('chai');

const createPushNotificationsJobs = require('./8-job');

describe('createPushNotificationsJobs', () => {
  before(() => queue.testMode.enter());
  afterEach(() => queue.testMode.clear());
  after(() => queue.testMode.exit());

  it('display a error message if jobs is not an array', () => {
    const list = {
      phoneNumber: '4153518780',
    }
    expect(() => createPushNotificationsJobs(list, queue)).to.throw(Error, 'Jobs is not an array')
  });
  it('create two new jobs to the queue', () => {
    const jobs = [
      {
        honeNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ]

    createPushNotificationsJobs(jobs, queue)
    expect(queue.testMode.jobs.length).to.equal(2)

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3')
  });
});
