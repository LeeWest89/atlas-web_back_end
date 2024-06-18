// creates StudentsController class and static methods getAllstudents and getAllStudentsByMajor
import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    const dbPath = '../../database.csv';

    readDatabase(dbPath)
      .then((studentNames) => {
        response.status(200);
        let infoOutput = 'This is the list of our students\n';
        let students = 0;
        const fields = Object.keys(studentNames);

        fields.forEach((field) => {
          students += studentNames[field].length;
        });

        infoOutput += `Number of students: ${students}\n`;

        const sortedFields = fields.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

        sortedFields.forEach((field) => {
          infoOutput += `Number of students in ${field}: ${studentNames[field].length}. List: ${studentNames[field].join(', ')}\n`;
        });

        response.send(200, infoOutput);
      })

      .catch(() => response.send(500, 'Cannot load the database'));
  }

  static getAllStudentsByMajor(request, response) {
    const major = request.query.field;
    const dbPath = '../../database.csv';

    if (major !== 'CS' && major !== 'SWE') {
      response.send(500, 'Major parameter must be CS or SWE');
    } else {
      readDatabase(dbPath)
        .then((studentNames) => {
          const students = studentNames[major];

          response.send(200, `List: ${students.join(', ')}`);
        })
        .catch(() => response.send(500, 'Cannot load the database'));
    }
  }
}

module.export = StudentsController;
