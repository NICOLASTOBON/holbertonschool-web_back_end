export default function createIteratorObject(report) {
  const values = [];

  const departmentsList = Object.values(report.allEmployees);
  const department = [...departmentsList];
  for (const value of department) {
    values.push(...value);
  }

  return values;
}
