# Gen-pyckage

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![test](https://github.com/iamgodot/gen-pyckage/actions/workflows/test.yml/badge.svg)](https://github.com/iamgodot/gen-pyckage/actions/workflows/test.yml)

Gen-pyckage is a python package template based on [cookiecutter](https://github.com/audreyr/cookiecutter).

## Features

- Use right away, without broken pieces
- Fulfilled Python package structure with
  - Setup.cfg
  - MANIFEST.in
  - Pyproject.toml
- GitHub Actions workflows for CI/CD
- Customizable hooks(from cookiecutter) for generating

## Inspired by

- https://github.com/audreyfeldroy/cookiecutter-pypackage
- https://keepachangelog.com/en/1.0.0/

## Usage

```bash
# Install cookiecutter
pip3 install --user cookiecutter

# Generate your project, just follow the prompts and fill out
cookiecutter https://github.com/iamgodot/gen-pyckage

# Let's say your project slug is greeting
cd greeting

# Make a virtual environment and install requirements
make venv
source venv/bin/activate
make install

# Now everything is set, just test it out
make test
```

To use the `release` workflow, you have to add `PYPI_API_TOKEN` in repo secrets.

## Contributing

Forks and pull requests are welcome.

For any questions or suggestions, please [open an issue](https://github.com/iamgodot/gen-pyckage/issues), thank you.

## License

[MIT](LICENSE)
