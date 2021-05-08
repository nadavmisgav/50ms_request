const express = require("express");
const fs = require("fs");
const url = require("url");
const os = require("os");

const port = 8080;
const app = express();

app.use("/public", express.static(__dirname + "/public"));
app.use(express.static(__dirname + "/public"));

app.get("/", (req, res) => {
  console.log(`Received get request`);
  res.send("Hello World!");
});

app.post("/", function (request, respond) {
  console.log(`Received post request`);
  var body = "";
  filePath = __dirname + "/public/data.txt";
  request.on("data", function (data) {
    body += data;
  });

  request.on("end", function () {
    fs.appendFile(filePath, body, function () {
      respond.end();
    });
  });
});

app.listen(port, () => {
  console.log(`Server listening at ${os.hostname()}:${port}`);
});
