const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const PORT = 1245;
const PATH = process.argv[2];

app.get('/', (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents(PATH)
    .then((data) => {
      const { students, studentsByCS, studentsBySWE } = data;
      res.write('This is the list of our students\n');
      res.write(`Number of students: ${students.length}\n`);
      res.write(`Number of students in CS: ${studentsByCS.length}. List: ${studentsByCS.join(', ')}\n`);
      res.write(`Number of students in SWE: ${studentsBySWE.length}. List: ${studentsBySWE.join(', ')}`);

      res.statusCode = 200;
      res.end();
    }).catch((err) => {
      res.status(500).send(err.message);
    });
});

app.listen(PORT);

module.exports = app;
