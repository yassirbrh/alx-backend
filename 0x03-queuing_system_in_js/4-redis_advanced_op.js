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

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, print);
}


async function displaySchoolValue(schoolName) {
	console.log(await promisify(client.get).bind(client)(schoolName));
}

async function run() {
	client.hset('HolbertonSchools', 'Portland', 50, print);
	client.hset('HolbertonSchools', 'Seattle', 80, print);
	client.hset('HolbertonSchools', 'New York', 20, print);
	client.hset('HolbertonSchools', 'Bogota', 20, print);
	client.hset('HolbertonSchools', 'Cali', 40, print);
	client.hset('HolbertonSchools', 'Paris', 2, print);
	try {
		console.log(await promisify(client.hgetall).bind(client)('HolbertonSchools'));
	} catch(err) {
		console.log('Error: ', err)
	}
}

run();
