
var express =   require('express');
var model = require('./models/post')
var api = require('./routes/api');
var app = express();
app.use('/api', api);
module.exports  =   app;

