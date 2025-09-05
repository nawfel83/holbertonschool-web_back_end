import readDatabase from '../utils.js';

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(process.argv[2])
      .then((fields) => {
        let output = 'This is the list of our students';
        
        const sortedFields = Object.keys(fields).sort((a, b) => 
          a.toLowerCase().localeCompare(b.toLowerCase())
        );
        
        sortedFields.forEach((field) => {
          output += `\nNumber of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
        });
        
        response.status(200).send(output);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
  
  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    
    readDatabase(process.argv[2])
      .then((fields) => {
        const students = fields[major] || [];
        response.status(200).send(`List: ${students.join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
