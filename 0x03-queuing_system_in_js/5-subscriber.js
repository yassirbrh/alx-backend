#!/usr/bin/node

import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
	console.log('Redis client connected to the server');
});

client.on('error', (err) => {
	console.log('Redis client not connected to the server:', err.toString());
});

client.subscribe('holberton school channel');

client.on('message', (_error, msg) => {
	console.log(msg);
	if (msg == 'KILL_SERVER') {
		client.unsubscribe();
		client.quit();
	}
});
