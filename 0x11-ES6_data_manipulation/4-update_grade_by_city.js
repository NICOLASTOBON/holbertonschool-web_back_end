/* eslint-disable */

import getStudentsByLocation from './2-get_students_by_loc';

function updateStudentGradeByCity(students, city, newGrades) {
  const studentByLocation = getStudentsByLocation(students, city);

  studentByLocation.map((student) => {
    student.grade = 'N/A';

    newGrades.filter((newGrade) => {
      if (newGrade.studentId === student.id) {
        student.grade = newGrade.grade;
      }
    });
  });

  return studentByLocation;
}

export default updateStudentGradeByCity;
