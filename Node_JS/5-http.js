//  create a small HTTP server using the http module
const http = require('http');

const countStudents = require('./3-read_file_async');

const dbName = process.argv.slice(2)[0];
const PORT = 1245;

const app = http.createServer(async (req, res) => {
  const { url } = req;

  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (url === '/') {
    res.write('Hello Holberton School!');
    res.end();
  } else if (url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const { studentNames, students } = await countStudents(dbName);

      res.write(`Number of students: ${students}\n`);
      for (const [field, firstnames] of Object.entries(studentNames)) {
        res.write(`Number of students in ${field}: ${firstnames.length}. List: ${firstnames.join(', ')}\n`);
      }
      res.end();
    } catch (error) {
      res.end(error.message);
    }
  }
  res.statusCode = 404;
  res.end();
});

app.listen(PORT, () => {});

module.export = app;
