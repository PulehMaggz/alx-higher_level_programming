#!/usr/bin/node

const request = require('request');

const url = process.argv[2]; // First argument: API URL

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const tasks = JSON.parse(body);
  const completedTasks = {};

  tasks.forEach(task =>
