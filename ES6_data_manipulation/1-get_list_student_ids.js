export default function getListStudentIds(ids) {
  if (!Array.isArray(ids)) {
    return [];
  }
  return ids.map((id) => id.id);
}
