var express = require("express");
var router = express.Router();
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const fs = require("fs");
const fetch = require("node-fetch");
const build_code = "12345";
const spawn = require("child_process").spawn;
const readline = require("readline");
const cheerio = require('cheerio');


const PYTHON_PATH ="/Library/Developer/CommandLineTools/usr/bin/python3";
var predictor_process;
var rl; //interface to read from the predictor
var building_model = false;
var res_queue = [];
var builder;

function stripTag(document, tagname) {
  var scripts = document.getElementsByTagName(tagname);
  var i = scripts.length;
  while (i--) {
    scripts[i].parentNode.removeChild(scripts[i]);
  }
}

/*add texts to the data bank from the given url */
router.post("/addText", async function (req, res, next) {
  try {
    const response = await fetch(req.body.url);
    const body = await response.text();

    const dm = new JSDOM(body);
    res.status(200).send();

    var data = dm.window.document;
    stripTag(data,'script');


    data = data.body.textContent;

    
    data = data.replace(/\s{2,}/g, " ").replace(/[.,\"!\?]/g,"").toLowerCase();
    fs.appendFileSync(
      __dirname + "/../ML/data/data.txt",
      "\n" + data,
      (err) => {}
    );
  } catch (e) {
    console.log(e);
    res.status(400).send();
  }
});

router.post("/buildModel", async function (req, res) {
  var code = req.body.code;

  try {
    if (code === build_code && !building_model) {
      building_model = true;
      res.json({ msg: "Building the model" }).status(200);

      if (predictor_process) {
        predictor_process.kill();
        predictor_process = null;
      }

      builder = spawn(PYTHON_PATH, ["'"+__dirname+"/../ML/builder.py'"],{shell:true});

      builder.stderr.pipe(process.stdout);
      
      builder.on("exit", () => {
        building_model = false;
      });

      return;
    }

    res.json({ msg: "can not start model building!" }).status(400);
  } catch (e) {
    console.log(e);
  }
});

const predict = (req, res) => {
  if (building_model) {
    res.json({ msg: "Training the model. Please wait!" }).status(400);
    return;
  }

  //check if the model exits
  //and then load the process if it is not
  //already loaded before
  if (!predictor_process) {
    //check if the model exist
    try {
      if (fs.existsSync(__dirname + "/../ML/data/next_words.h5")) {
      }
    } catch (e) {
      res
        .json({ msg: "No Model were built. Please train the model first!" })
        .status(400);
      return;
    }


    //load the model
    predictor_process = spawn(PYTHON_PATH, ["'"+__dirname + "/../ML/predictor.py'"],{shell:true});


    predictor_process.stderr.pipe(process.stdout);
    rl = readline.createInterface({ input: predictor_process.stdout });

    rl.on("line", (line) => {
      var res = res_queue.shift();
      res.json({ prediction: line.split(",") }).status(200);
    });
  }

  res_queue.push(res);
  var text = req.body.prompt.toLowerCase().replace(/\s{2,}/g, " ").replace(/[.,\"!\?]/g,"");

  predictor_process.stdin.cork();
  predictor_process.stdin.write(req.body.prompt + "\n");
  predictor_process.stdin.uncork();
};

router.post("/predict", (req, res) => {
  try {
    predict(req, res);
  } catch (e) {
    console.log(e);
  }
});

module.exports = router;
