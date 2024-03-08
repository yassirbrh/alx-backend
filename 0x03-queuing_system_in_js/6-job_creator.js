#!/usr/bin/node

import { createQueue } from 'kue';

const queue = createQueue();
const jobData = {phoneNumber: '0999999999', message: 'New Account !!'};

const job = queue.create('push_notification_code', jobData).save(function(err) {
    if (err) {
        console.error('Error creating job:', err);
    } else {
        console.log('Notification job created:', job.id);
    }
});

queue.on('job complete', function(id, result) {
    console.log(`Notification job completed`);
});

queue.on('job failed', function(id, result) {
    console.log('Notification job failed');
});
