// creates StudentsController class and static methods getAllstudents and getAllStudentsByMajor
import path from 'path';
import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    const dbPath = path.resolve(process.cwd(), 'database.csv');

    readDatabase(dbPath)
      .then((studentNames) => {
        response.status(200);
        let infoOutput = 'This is the list of our students\n';
        const fields = Object.keys(studentNames);
        const sortedFields = fields.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

        sortedFields.forEach((field, index) => {
          infoOutput += `Number of students in ${field}: ${studentNames[field].length}. List: ${studentNames[field].join(', ')}`;
          if (index < sortedFields.length - 1) {
            infoOutput += '\n';
          }
        });

        response.status(200).send(infoOutput);
      })

      .catch((error) => {
        console.error('Error reading database:', error);
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const major = request.params.majorto;
    const dbPath = path.resolve(process.cwd(), 'database.csv');

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(dbPath)
      .then((studentNames) => {
        if (studentNames[major]) {
          const students = studentNames[major];
          response.status(200).send(`List: ${students.join(', ')}`);
        }
      })
      .catch((error) => {
        console.error('Error reading database:', error);
        response.status(500).send('Cannot load the database');
      });
  }
}

module.exports = StudentsController;
