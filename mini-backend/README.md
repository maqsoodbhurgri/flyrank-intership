# Mini Backend API

A simple backend server built using Python and Flask.

## Features

* JSON API responses
* Two endpoints
* Tested using Browser and curl
* Ready for GitHub deployment

## Endpoints

### Home Endpoint

```bash
GET /
```

Response:

```json
{
  "message": "Mini Backend API is running successfully",
  "status": "success"
}
```

### About Endpoint

```bash
GET /about
```

Response:

```json
{
  "name": "Maqsood Ahmed",
  "role": "Backend Learner",
  "project": "Mini Backend API"
}
```

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Server runs on:

```text
http://127.0.0.1:5000
```
