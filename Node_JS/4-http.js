//  create a small HTTP server using the http module
const http = require('http');

const PORT = 1245;

const app = http.createServer((req, res) => {
  res.writeHeader(200, { 'Content-Type': 'text/plain' });
  res.end('Hello Holberton School!');
});

app.listen(PORT, () => {});

module.export = app;
