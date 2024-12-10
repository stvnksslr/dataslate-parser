# Dataslate Parser

[![Build](https://github.com/stvnksslr/dataslate-parser/actions/workflows/build.yml/badge.svg)](https://github.com/stvnksslr/dataslate-parser/actions/workflows/build.yml)[![Deploy](https://github.com/stvnksslr/dataslate-parser/actions/workflows/deploy.yaml/badge.svg)](https://github.com/stvnksslr/dataslate-parser/actions/workflows/deploy.yaml)

This project is to take in battlescribe roster files and output them into easily printable sheets or cards since the current output is awful.

## Requirements

- Python 3.11+

## Setup

### UV
1. uv sync
2. uv run python -m src.main


### Run App

To run application from python environment :

- from base directory `uvicorn src.main:app`


### Icons 

The icons are available on https://github.com/jermarchand/wh40k-icon/releases/tag/v0.2.0