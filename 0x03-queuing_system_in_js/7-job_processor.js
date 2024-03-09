#!/usr/bin/node

import { createQueue } from 'kue';

const blacklisted_nums = ['4153518780', '4153518781']; // More descriptive name
const notificationQueue = createQueue(); // Specific queue purpose

function sendNotification(phoneNumber, message, job, done) {
  const totalAttempts = 2;
  let remainingAttempts = totalAttempts;

  const sendInterval = setInterval(() => {
    const attemptsUsed = totalAttempts - remainingAttempts;
    if (attemptsUsed >= totalAttempts / 2) {
      job.progress(attemptsUsed, totalAttempts); // Update progress for every other attempt
    }

    if (blacklisted_nums.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(sendInterval);
      return; // Exit the loop if number is blacklisted
    }

    if (remainingAttempts === 0) {
      console.log(
        `Sending notification to ${phoneNumber},`,
        `with message: ${message}`,
      );
    }

    remainingAttempts--;
    if (remainingAttempts === 0) {
      done();
    }
  }, 1000);
};

notificationQueue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

