# python-otel-example

A simple example for how to setup OpenTelemetry in code and send traces to aspecto

You need to set in `tracing.py`:
1. `"your-service-name"` - to the name of your service, which you can later be used to search / filter / alert / sample etc in aspecto platform
2. `"your-aspecto-token"` which you can find [here](https://app.aspecto.io/integration/tokens)

## Installation
This project uses `pipenv`. To run:
```bash
pipenv install
pipenv run python main.py
```
