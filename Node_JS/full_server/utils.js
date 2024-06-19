// read the database asynchronously and returns a promise, basing it off 3-read_file_async.js
const fs = require('fs');

function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n');
      const studentNames = {};
      let i = 1;

      for (; i < lines.length; i += 1) {
        const line = lines[i].trim();

        if (line) {
          const [firstname, , , field] = line.split(',');

          if (firstname && field) {
            if (!studentNames[field]) {
              studentNames[field] = [];
            }
            studentNames[field].push(firstname);
          }
        }
      }

      resolve(studentNames);
    });
  });
}

module.exports = readDatabase;
