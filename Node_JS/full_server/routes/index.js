// creating function the controls Routing
const express = require('express');
const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

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
