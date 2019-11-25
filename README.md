# Inria Digital Accessibility MOOC API

This web application handles Inria MOOC Accessibility web player events. Its main purpose is to act as a gateway between the web client and an [ElasticSearch](https://www.elastic.co/products/elasticsearch) server.

## Requirements

* [python](https://www.python.org) `=3.6`
* [Pipenv](https://pipenv.kennethreitz.org/en/latest/)

## Installation

```sh
pipenv install
```

For development purpose, you also should install additional packages:

```sh
pipenv install --dev
```

The application assumes ElasticSearch is used to save records. If no ElasticSearch server can be found, it will just output errors and return `500` errors.

Most straightforward installation requires Docker. Just `cd` into the application directory and run `docker-compose up`.  
Running this command will start an ElasticSearch server on `http://localhost:9200` and a Kibana instance on `http://localhost:5601` to visualize events.

### Linting

```sh
pipenv run lint # runs pycodestyle
pipenv run lint_fix # fixes malformed code
```

## Run the application

### Development

```sh
cd /path/to/mooc-accessibility-api
pipenv run serve_dev
```

Application will be served through built-in Flask server on port `3001`.

### Production

[Gunicorn](https://gunicorn.org/) is provided as a dependency, and should be the prefered way to serve the application in production.

```sh
# numbers of workers depend on the machine hosting the application
pipenv run gunicorn --workers=3 --bind=127.0.0.1:8000 wsgi:application
```

### Note About Logging

Logs are written to `STDERR` and `STDOUT`. This can be overridden by configuring the wsgi app container.

### Environment Variables

The `.env` file hosts a few variables you may need to change before running the application.
