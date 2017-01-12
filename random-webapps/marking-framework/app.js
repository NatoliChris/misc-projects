var express = require('express');
var request = require('request');
var exphbs = require('express-handlebars');

/*-----------
 * Express
 *-----------
 */

var app = express();
app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');
app.use(express.static('public'));

/*-------------
 * STATIC DIRS
 *-------------
 */

app.use('/public/css', express.static(__dirname + '/public/css'));
app.use('/public/scripts', express.static(__dirname + '/public/scripts'));
app.use('/node_modules', express.static(__dirname + '/node_modules'));


var debug = false;

app.get('/', function(req, res) {
	res.render('index', {heading: 'INFO2120'});
});


var server = app.listen(8001, function() {
	var host = server.address().address;
	var port = server.address().port;

	console.log("Listening on %s:%s", host, port);
});
