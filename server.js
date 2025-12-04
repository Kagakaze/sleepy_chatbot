const http = require("http");
const server = http.createServer();

const fs = require("fs");

const port = 8082;

server.on("request", (req, res) => {
    if (req.url === "/images") {
      res.end(fs.readFileSync("./images.html", "utf-8"));
    } else {
      res.end(fs.readFileSync("./index.html", "utf-8"));
    }
  });
  
  server.listen(port, () => {
    console.log("Server running");
  });