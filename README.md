# Dataslate Parser

![](https://github.com/stvnksslr/dataslate-parser/workflows/build/badge.svg)
![](https://github.com/stvnksslr/dataslate-parser/workflows/deploy/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/86bd40b6d3fd037140d4/maintainability)](https://codeclimate.com/github/stvnksslr/dataslate-parser/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/86bd40b6d3fd037140d4/test_coverage)](https://codeclimate.com/github/stvnksslr/dataslate-parser/test_coverage)

![](https://img.shields.io/github/v/release/stvnksslr/dataslate-parser?label=Latest%20Release)
![](https://img.shields.io/github/v/release/stvnksslr/dataslate-parser?label=Deployed%20Release)

This project is to take in battlescribe roster files and output them into easily printable sheets or cards since the current output is awful.

## Requirements

- Python 3.7+

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
