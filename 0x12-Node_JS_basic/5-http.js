const http = require('http');
const countStudents = require('./3-read_file_async');

const PATH = process.argv[2];
const PORT = 1245;

async function router(req, res) {
  const { students, studentsByCS, studentsBySWE } = await countStudents(PATH);

  if (req.url === '/students') {
    res.write(`Number of students: ${students.length}\n`);
    res.write(`Number of students in CS: ${studentsByCS.length}. List: ${studentsByCS.join(', ')}\n`);
    res.write(`Number of students in SWE: ${studentsBySWE.length}. List: ${studentsBySWE.join(', ')}\n`);
    res.end();
  } else {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('Hello Holberton School!');
    res.end();
  }
}

const app = http.createServer(router).listen(PORT);

module.exports = app;
