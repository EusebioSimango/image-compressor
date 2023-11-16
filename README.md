# Image Compressor

## Run it

### Using Docker

First you may have [docker](https://www.docker.com/) installed on your machine, and then clone this repository:

```bash
$ git clone https://github.com/EusebioSimango/image-compressor

$ cd image-compressor

$ docker-compose up -d
```

After that the server should be listening on the port `8080`

### Using Virtual environment

First you may have at-least python version 3.8:

```bash
$ git clone https://github.com/EusebioSimango/image-compressor

$ cd image-compressor

$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r requirements.txt

$ python3 main.py
```

After that the server should be listening on the port `8080`

### Usage

After having it running, you can send an http request using any client, or just access the docs to send the request on `http://localhost:8080/docs`

#### The request example using javascript's `fetch` api

```js
const fs = require("fs");
const FormData = require("form-data");
const fetch = require("node-fetch");
const formData = new FormData();

formData.append("file", fs.createReadStream("/path/to/the/image.png"));

let options = {
  method: "POST",
  headers: {
    "Content-Type": "multipart/form-data; boundary=---011000010111000001101001",
  },
};

options.body = formData;

fetch("http://localhost:8080/process-image", options)
  .then((res) => res.json())
  .then((json) => console.log(json))
  .catch((err) => console.error("error:" + err));
```
