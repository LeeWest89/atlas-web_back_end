// Creating a job

import kue from 'kue';

const que = kue.createQueue();

const jobInfo = {
  phoneNumber: 'string1',
  message: 'string2',
};

const job = que.create('push_notification_code', jobInfo).save((error) => {
  if (!error) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
