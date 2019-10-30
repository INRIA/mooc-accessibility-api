# Inria Digital Accessibility MOOC API

This web application handles Inria MOOC Accessibility web player events. Its main purpose is to act as a gateway between the web client and the [ElasticSearch](https://www.elastic.co/products/elasticsearch) server.

## Requirements

* [python](https://www.python.org) `=3.6`
* [Pipenv](https://pipenv.kennethreitz.org/en/latest/)

## Installation

```sh
pipenv install
```

## Development

You should install additional packages for development purpose.

```sh
pipenv install --dev
```

ElasticSearch is required in order to save records. The application will run if no ElasticSearch server can be found, but it will simply output errors.

Simplest installation requires Docker. Just `cd` into the application directory and run `docker-compose up`.
This will start an ElasticSearch server (on `localhost:9200`) and a Kibana instance (on `localhost:5601`) to visualize events.

### Linting

```sh
pipenv run lint # runs pycodestyle
pipenv run lint_fix # fixes malformed code
```

## Run the application

```sh
cd /path/to/mooc-accessibility-api
pipenv run serve
```

### Note About Logging

Logs are written to `STDERR`. This can be overridden by specifying a custom logger in the app.

### Environment Variables

The .env file hosts a few variables you may need to change before running the application.
