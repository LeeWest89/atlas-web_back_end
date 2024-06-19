// creating function the controls Routing
import express from 'express';
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

function controlRoute(app) {
  const router = express.Router();
  app.use('/', router);

  router.get('/', (request, resolve) => {
    AppController.getHomepage(request, resolve);
  });

  router.get('/students', (request, resolve) => {
    StudentsController.getAllStudents(request, resolve);
  });

  router.get('/students/:majorto', (request, resolve) => {
    StudentsController.getAllStudentsByMajor(request, resolve);
  });
}

module.exports = controlRoute;
