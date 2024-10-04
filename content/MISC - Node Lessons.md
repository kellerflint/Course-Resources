# Node Basics and Hosting

### Installing Node

Downloads:
- [Node.js (nodejs.org)](https://nodejs.org/en)
- [Visual Studio Code - Code Editing. Redefined](https://code.visualstudio.com/)

You can test that node installed successfully by opening your terminal and typing `node -v`.

### Project Setup and Hello World App

##### Terminal Commands from Video

Create the project:
```bash
npm init -y
```

Install express:
```bash
npm i express ejs
```

Create app.js file in the project root with the following:
```js
const express = require('express');

const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
    res.send('Hello World');
});

app.listen(PORT, () => {
    console.log(`Server is running on port http://localhost:${PORT}`);
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

You can stop the node app by pressing control + c in the terminal.

---

Create a "views" folder and restructure your project files:
```
your-project/
├── views/
│   └── home.ejs (formerly index.html)
├── public/
│   └── styles/
│       └── home.css (formerly pizza-styles.css)
│   └── images/
│       └── images here...
└── app.js
```

Update app.js:
```js
const express = require('express');

const app = express();
const PORT = 3000;

app.use(express.urlencoded({ extended: false }));
app.use(express.static('public'));

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    res.render('home');
});

app.post('/success', (req, res) => {
    const data = req.body;
    res.send(data);   
});

app.listen(PORT, () => {
    console.log(`Server is running on port http://localhost:${PORT}`);
});
```

To see changes, you will need to stop and restart the app.

Deployment Steps:
- Zip the project file
- Upload to your home directory in WH4S
- Extract
- "Setup Node.js App"
- Set the application root to the project folder's name
- Create it
