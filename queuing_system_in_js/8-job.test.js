// test for 8-job.js

const createPushNotificationsJobs = require('./8-job.js');
const kue = require('kue');
const assert = require('assert');
const sinon = require('sinon');

describe('createPushNotificationsJobs', function() {
  let que;
  const jobs = [
    {
      phoneNumber: '9187775555',
      message: 'This is the code 1234 to verify your account',
    },
    {
      phoneNumber: '4057775555',
      message: 'This is the code 4321 to verify your account',
    },
  ];
  let conSpy;

  beforeEach(function() {
    que = kue.createQueue();
    que.testMode.enter();
    conSpy = sinon.spy(console, 'log');
  });

  afterEach(function() {
    que.testMode.clear();
    que.testMode.exit();
    conSpy.restore();
  });

  it('should show error if jobs isnt an array', function() {
    assert.throws(() => createPushNotificationsJobs('!array', que), new Error('Jobs is not an array'));
  });

  it('should check jobs existance', function() {
    createPushNotificationsJobs(jobs, que);
    const job = que.testMode.jobs[0];

    assert.ok(que.testMode.jobs.find(j => j.id === job.id));
  });

  it('should make 2 new jobs', function() {
    const saveSpy = sinon.spy(kue.Job.prototype, 'save');

    createPushNotificationsJobs(jobs, que);

    assert.strictEqual(que.testMode.jobs.length, 2);
    assert(saveSpy.calledTwice);
    saveSpy.restore();
  });

  it('should show complete in console', function(done) {
    createPushNotificationsJobs(jobs, que);
    const job = que.testMode.jobs[0];

    job.on('complete', () => {
      assert(conSpy.calledWith(`Notification job ${job.id} completed`));
      done();
    });

    job.emit('complete');

  });

  it('should show failed in console', function(done) {
    createPushNotificationsJobs(jobs, que);
    const job = que.testMode.jobs[0];

    job.on('failed', (error) => {
      assert(conSpy.calledWith(`Notification job ${job.id} failed: ${error}`));
      done();
    });

    job.emit('failed');

  });

  it('should show progress in console', function(done) {
    createPushNotificationsJobs(jobs, que);
    const job = que.testMode.jobs[0];

    job.on('progress', (progress) => {
      assert(conSpy.calledWith(`Notification job ${job.id} ${progress}% complete`));
      done();
    });

    job.emit('progress', 75);

  });
});
