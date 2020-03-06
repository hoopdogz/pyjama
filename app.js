const fs = require('fs')
const path = require('path')
const express = require('express')
const {spawn} = require('child_process');

const app = express()
const port = process.env.PORT || 4000

const public_path = path.join(__dirname, './public')
const db_path = path.join(__dirname, './py')
app.use(express.static(public_path))

app.get('', (req, res) => {
  res.sendFile(public_path+'/index.html')
})

app.get('/py/:name', (req, res) => {
  try {
    var dataToSend

    let python
    console.log(req.query.params)

    if (req.query.params) {
      // python = spawn('python', [`${db_path}/${req.params.name}.py`,`${req.query.params}`])
      let args = [`${db_path}/${req.params.name}.py`]
      let param_split = (req.query.params).split(" ")
      args = args.concat(param_split)
      console.log(args)
      python = spawn('python', args)
    } else {
      python = spawn('python', [`${db_path}/${req.params.name}.py`])
    }

    python.stdout.on('data', function (data) {
      console.log(`Run ${req.params.name}.py`)
      dataToSend = data.toString()
     })
     python.on('close', (code) => {
      console.log(`End ${req.params.name}.py (${code})`)
      res.send(dataToSend)
    })
  } catch {
    res.status(404).send()
  }
})

app.listen(port, () => {
  console.log(`I am running on port ${port}.`)
})