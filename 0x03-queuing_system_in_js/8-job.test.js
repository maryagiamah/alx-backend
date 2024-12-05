import { createQueue } from 'kue';
const { expect } = require('chai');

import createPushNotificationsJobs from './8-job.js';

const queue = createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should validate the queue length', () => {
    const jobs = [
      { phoneNumber: '567890', message: 'This is your code 5678' },
      { phoneNumber: '453910', message: 'This is your code 4591' },
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });
});
