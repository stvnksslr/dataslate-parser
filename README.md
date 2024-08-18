# Dataslate Parser

[![Build](https://github.com/stvnksslr/dataslate-parser/actions/workflows/build.yml/badge.svg)](https://github.com/stvnksslr/dataslate-parser/actions/workflows/build.yml)[![Deploy](https://github.com/stvnksslr/dataslate-parser/actions/workflows/deploy.yaml/badge.svg)](https://github.com/stvnksslr/dataslate-parser/actions/workflows/deploy.yaml)

This project is to take in battlescribe roster files and output them into easily printable sheets or cards since the current output is awful.

## Requirements

- Python 3.11+

## Setup

### Poetry

1. `poetry install`
2. `poetry shell`
3. `pytest`

### Pip

1. `python -m venv .venv`
2. `activate with your preferred method`
3. `pip install -r requirements-dev.txt`
4. `pytest`

### Run App

To run application from python environment :

- from base directory `uvicorn src.main:app`


### Icons 

The icons are available on https://github.com/jermarchand/wh40k-icon/releases/tag/v0.2.0