// create a small Express server
const express = require('express');
const controlRoute = require('./routes/index');

const app = express();
const PORT = 1245;

controlRoute(app);

app.listen(PORT, () => {});

module.exports = app;
