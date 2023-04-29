# Create Python App

Test

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![test](https://github.com/iamgodot/create-python-app/actions/workflows/test.yml/badge.svg)](https://github.com/iamgodot/create-python-app/actions/workflows/test.yml)

Create-python-app is a python package template based on [cookiecutter](https://github.com/audreyr/cookiecutter).

## Features

- Integrate [pdm](https://github.com/pdm-project/pdm) for dependency management.
- Proper github workflows setup.
- Delicate Makefile.

## Inspired by

- https://github.com/audreyfeldroy/cookiecutter-pypackage
- https://keepachangelog.com/en/1.0.0/

## Usage

```bash
# Install cookiecutter
pipx install cookiecutter

# Generate your project, just follow the prompts and fill out
cookiecutter https://github.com/iamgodot/create-python-app

# Let's say your project slug is greeting
cd greeting

# Make sure you have pdm installed
make install
make test
```

To use the `release` workflow, you have to add `PYPI_API_TOKEN` in repo secrets.

## Contributing

For any questions or suggestions, please [open an issue](https://github.com/iamgodot/create-python-app/issues).

## License

[MIT](LICENSE)
