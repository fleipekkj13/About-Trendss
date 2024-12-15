const express = require('express');
const app = express();
const cors = require('cors')
const { spawn } = require('child_process');
app.use(cors())
let jsonData = '';

const port = 3000;

app.get('/', (req, res) => {
    res.send("Hello, world!");
})

app.get('/search' ,(req,res) => {
    const pythonProcess = spawn('python', ['./python/getData.py'])
    pythonProcess.stdout.on('data', (data) => {
        jsonData += data.toString();
        const dados = JSON.parse(jsonData)
        console.log(dados)
        res.send(dados)
    })
})

app.listen(port, () => {
    console.log(`Example app listening on port http://localhost:${port}`);
})