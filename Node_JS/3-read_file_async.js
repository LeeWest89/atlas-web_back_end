// function to attemp to read database asynchronously
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n');
      const studentNames = {};
      let students = 0;

      for (let i = 1; i < lines.length; i += 1) {
        const line = lines[i].trim();

        if (line) {
          const [firstname, lastname, age, field] = line.split(',');

          if (firstname && lastname && age && field) {
            if (!studentNames[field]) {
              studentNames[field] = [];
            }
            studentNames[field].push(firstname);
            students += 1;
          }
        }
      }

      const text = [`Number of students: ${students}`];

      for (const [field, firstnames] of Object.entries(studentNames)) {
        text.push(`Number of students in ${field}: ${firstnames.length}. List: ${firstnames.join(', ')}`);
      }

      resolve(text);
    });
  });
}

module.exports = countStudents;
