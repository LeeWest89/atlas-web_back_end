// creating function the controls Routing
import express from 'express';
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

function controlRoute(app) {
  const router = express.Router();
  app.use('/', router);

  router.get('/', AppController.getHomepage);
  router.get('/students', StudentsController.getAllStudents);
  router.get('/students/:major', StudentsController.getAllStudentsByMajor);
}

module.exports = controlRoute;
