# Forwarder

## Installing dependencies

Python 3.7 or higher is required. https://www.python.org/downloads/

Runtime Python dependencies are listed in requirements.txt at the root of the
repository. They can be installed from a terminal by running
```
pip install -r requirements.txt
```

### Development dependencies

Development dependencies (including all runtime dependencies) can be installed by using the following command 

```
pip install -r requirements-dev.txt
```

`black`, `flake8` and `mypy` can be used as a pre-commit hook (installed by [pre-commit](https://pre-commit.com/)).
You need to run
```
pre-commit install
```
once to activate the pre-commit check.
To test the hooks run
```
pre-commit run --all-files
```
This command can also be used to run the hooks manually.

## Running the application

Run the python script forwarder_launch.py`

## Docker

To build a docker image
```
docker build . -t forwarder
```

Use environment variables to pass command line arguments, for example
```
docker run -e CONFIG_TOPIC="localhost/config" -e STATUS_TOPIC="localhost/status" forwarder
```

## C++ Forwarder features not replicated here

Won't do unless we discover it is necessary:
- Configure forwarding from json file (already agreed to remove from C++ codebase)
- Forwarding to multiple Kafka clusters
- Forwarding same PV with different converters (can be added separately so it is just a performance improvement, if you would ever want to do this)
