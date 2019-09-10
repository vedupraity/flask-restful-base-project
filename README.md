
# Flask-RESTful Project

This is a Flask project with Flask-RESTful integration to quickly start building RESTful APIs.

**Author**: Vedprakash Upraity [GitHub](https://github.com/upraity95)

## Getting started

These instructions will get you a copy of this flask project up and running on your local machine for development and testing purposes.

### System Requirements

1. [Python]([https://www.python.org/](https://www.python.org/)) 3.6+
2. [virtualenv](https://virtualenv.pypa.io/en/latest/) 15.1.0

### Dependencies

1. [Flask](https://github.com/pallets/flask) 1.1.1
2. [Flask-RESTful](https://github.com/flask-restful/flask-restful) 0.3.7
3. [Python Decouple](https://github.com/henriquebastos/python-decouple/) 3.1

### Setup Virtual Environment and install dependencies

```sh
# Create Virtual Environment
$ virtualenv -p $(which python3.7) .venv
# Activate Virtual Environment
$ source .venv/bin/activate
# Install dependencies
$ pip install -r requirements.txt
```

### Environment configuration

Make a copy of file `settings.ini.example` as `settings.ini` in the directory `<project_root>/app/config`.

### Run the project

```sh
$ python server.py
```
