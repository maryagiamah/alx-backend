const { createQueue  }= require('kue');

const queue = createQueue();

const notify = {
  'phoneNumber': '+2349067897060',
  'message': 'You need to call Mrs Ameh',
}

const job = queue.create('push_notification_code', notify).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
