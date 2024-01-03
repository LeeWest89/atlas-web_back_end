export default function createEmployeesObject(departmentName, employees) {
  const departmentWorkers = {
    [departmentName]: employees,
  };

  return (departmentWorkers);
}
