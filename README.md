# Waste Classification using Deep Learning
This repository contains a deep learning model that utilizes transfer learning to classify pictures of waste into six classes:

* Biodegradable
* Cardboard
* Glass
* Metal
* Paper
* Plastic

## Prerequisites
* Python 3.6 or higher
* TensorFlow 2.0 or higher
* Flask

## Installation
1. Clone this repository to your local machine:

```
git clone https://github.com/Ecobin-Capstone/ecobin-model-api
```

2. Navigate to the repository directory:

```
cd ecobin-model-api
```

3. Create a virtual environment and activate it:

```
python3 -m venv venv
source venv/bin/activate
```

4. Install the required Python packages:

```
pip install -r requirements.txt
```

5. Rename .env.example to .env:
```
FLASK_DEBUG="False"
FLASK_PORT=80
```

## Usage
To run the model, follow these steps:

1. Start the Flask server:

```
python main.py
```

2. Open your web browser, and navigate to:

```
http://127.0.0.1:80/api
```

3. Open Postman
4. Add a new request and change the HTTP method to POST
5. Change the request url to `http://127.0.0.1:80`
6. ![model demo on postman](https://i.ibb.co/dbh65K5/screenshot-postman-demo.png)
7. Click send
8. The response should a JSON of predictions. Where the highest probability will be sorted first.

## Model Architecture
The model is based off of this repo: https://github.com/Ecobin-Capstone/ecobin-waste-classifier