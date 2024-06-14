export default function createReportObject(employeesList) {
  const object = {
    allEmployees: { ...employeesList },
    getNumberOfDepartments(employees) {
      return Object.keys(employees).length;
    },
  };

  return (object);
}
