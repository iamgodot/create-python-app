# {{cookiecutter.project_name}}

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

{{cookiecutter.project_description}}

## Installation

```bash
pip install {{cookiecutter.project_slug}}
```

## Usage

```
>>> from {{cookiecutter.project_slug}} import dict_subtract
>>> dict_subtract({}, {'a': 11})
{}
>>> dict_subtract({'a': 12}, {'a': 11})
{'a': 12}
>>> dict_subtract({'a': 11, 'b': 0}, {'a': 11})
{'b': 0}
```

## Support

>=python3.8

## Changelog

[Here](docs/CHANGELOG.md)

## License

[MIT](docs/LICENSE)

## Credits

This package was created with [cookiecutter](https://github.com/audreyr/cookiecutter) and [iamgodot/create-python-app](https://github.com/iamgodot/create-python-app) project template.
