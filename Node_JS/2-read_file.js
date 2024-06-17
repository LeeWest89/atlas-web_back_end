// function to attemp to read database
const fs = require('fs')

function countStudents(path) {
    let lines
    try {
        lines = fs.readFileSync(path);
    }

    catch (error) {
        throw new Error('Cannot load the database');
    }

    lines = fs.readFileSync(path, 'utf8').split('\n');
    const student_names = {}
    let students = 0;
    let i = 1;


    for (; i < lines.length; i++) {

        const line = lines[i];

        if (line.trim()) {
            const [firstname, lastname, age, field] = line.split(',');

            if (firstname && lastname && age && field) {
                if (!student_names[field]) {
                    student_names[field] = [];
                }
                student_names[field].push(firstname);
                students += 1;
            }
        }
    }

    console.log(`Number of students: ${students}`)
    for (const [field, firstnames] of Object.entries(student_names)) {
        console.log(`Number of students in ${field}: ${firstnames.length}. List: ${firstnames.join(', ')}`);
    }
}

module.exports = countStudents;
