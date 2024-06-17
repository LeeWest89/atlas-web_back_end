// recreate a small HTTP server using Express module

const express = require('express');

const countStudents = require('./3-read_file_async');

const app = express();
const PORT = 1245;
const dbName = process.argv.slice(2)[0];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const message = 'This is the list of our students\n';
  try {
    const data = await countStudents(dbName);
    res.send(`${message}${data.join('\n')}`);
  } catch (error) {
    res.send(`${error.message}`);
  }
});

app.listen(PORT, () => {});

module.exports = app;
