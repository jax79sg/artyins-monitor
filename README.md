
# Monitor For artyins deployment architecture
This is a submodule for the artyins architecture. Please refer to [main module](https://github.com/jax79sg/artyins) for full build details.

[![Build Status](https://travis-ci.com/jax79sg/artyins-monitor.svg?branch=master)](https://travis-ci.com/jax79sg/artyins-monitor)
[![Container Status](https://quay.io/repository/jax79sg/artyins-monitor/status)](https://quay.io/repository/jax79sg/artyins-monitor)

Refer to [Trello Task list](https://trello.com/c/ABdSKU5b) for running tasks.

---

## Table of Contents (Optional)

- [Usage](#Usage)
- [Virtualenv](#Virtualenv)
- [Tests](#Tests)

---

## Usage
The Monitor simply monitor a folder and call a designated endpoint when detected files in folder.

### config.py
The configuration file will indicate the paths and URL call endpoints.
```python
    DATAPATH="/shareddata/new/"
    PROCESSINGPATH="/shareddata/processing/"
    SUCCESSPATH="/shareddata/success/"
    FAILPATH="/shareddata/fail/"
    CREATEJOB_URL="http://jobsvc:9891/create_job"
    CHECK_INTERVAL=10
```

---

## Virtualenv
```shell
python3 -m venv venv
source venv/bin/activate
pip install --user -r requirements.txt`
```
---

## Tests 
This repository is linked to [Travis CI/CD](https://travis-ci.com/jax79sg/artyins-monitor).


