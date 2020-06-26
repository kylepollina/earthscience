#!/usr/bin/env bash

# Install the earthscience kernel using poetry
poetry install
poetry run python -m ipykernel install --user --name=earthscience
