// create a small Express server
import express from 'express';
import controlRoute from './routes/index';

const app = express();
const PORT = 1245;

controlRoute(app);

app.listen(PORT, () => {});

module.exports = app;
