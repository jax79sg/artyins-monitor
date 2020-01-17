
# Extraction Service For artyins deployment architecture
This is a submodule for the artyins architecture. Please refer to [main module](https://github.com/jax79sg/artyins) for full build details.

[![Build Status](https://travis-ci.com/jax79sg/artyins-extractionservice.svg?branch=master)](https://travis-ci.com/jax79sg/artyins-extractionservice)

Refer to [Trello Task list](https://trello.com/c/mKnW1fgx) for running tasks.

---

## Table of Contents (Optional)

- [Usage](#Usage)
- [Virtualenv](#Virtualenv)
- [Tests](#Tests)

---

## Usage
The extraction service can be called by a HTTP POST call. Primarily on http://webserverip:port/extract_content. It expects a json of the following format
```python
[{'filename':'file01.pdf',},{'filename':'file02.pdf'}]
```
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


