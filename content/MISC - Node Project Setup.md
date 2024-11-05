# Node Project Setup
### Installing Node
Downloads:
- [Node.js (nodejs.org)](https://nodejs.org/en)
- [Visual Studio Code - Code Editing. Redefined](https://code.visualstudio.com/)

You can test that node installed successfully by opening your terminal and typing `node -v`.

### Project Setup

Create a folder for the project. `cd` into the folder. This is the project root.

From the project root, initialize a new project:
```bash
npm init
```
- Entry Point: app.js
- Use defaults for the rest

Install express and ejs:
```bash
npm install express ejs
```

Create a "views" folder. Project structure should be:
```
your-project/
├── views/
│   └── home.ejs
│   └── views here...
├── public/
│   └── styles/
│       └── home.css
│       └── styles here...
│   └── images/
│       └── images here...
│   └── scripts/
│       └── scripts here...
├── package.json (generated from npm init)
├── package-lock.json (generated from npm init)
├── node_modules (generated from npm install)
└── app.js
```

Create app.js file in the project root with the following:
```js
// Get the express package 
const express = require('express');

// Instantiate an express (web) app
const app = express();

// Define a port number for the app to listen on
const PORT = 3000;

// Tell the app to encode data into JSON format
app.use(express.urlencoded({ extended: false }));

// Set your view (templating) engine to "EJS"
// (We use a templating engine to create dynamic web pages)
app.set('view engine', 'ejs');

// Define a "default" route, 
// e.g. jshmo.greenriverdev.com/reservation-app/
app.get('/', (req, res) => {
	// Log message to the server's console
	console.log("Hello, world - server!");

    // Return home page
    res.render('home');
});

// Define a "confirm" route, using the POST method
app.post('/confirm', (req, res) => {
    // Get the data from the form that was submitted
    // from the body of the request object
    let details = req.body;

    // Display the confirm page, pass the data
    res.render('confirm', { details: details });
})

// Tell the app to listen for requests on the designated port
app.listen(PORT, () => {
    console.log(`Server running on port http://localhost:${PORT}`)
});
```

Run node app from root in terminal:
```shell
node app.js
```

In your browser go to:
```
http://localhost:3000
```

You can stop the node app by pressing `CTRL + c` in the terminal.

To see changes made to the server, you will need to stop `CTRL + c` and restart `node app.js` the app.
