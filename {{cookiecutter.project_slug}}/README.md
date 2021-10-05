# {{cookiecutter.project_name}}

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

{{cookiecutter.project_description}}

## Installation

```bash
pip install {{cookiecutter.project_slug}}
```

## Usage

```
>>> from {{cookiecutter.project_slug}} import dict_substract
>>> dict_substract({}, {'a': 11})
{}
>>> dict_substract({'a': 12}, {'a': 11})
{'a': 12}
>>> dict_substract({'a': 11, 'b': 0}, {'a': 11})
{'b': 0}
```

## Support

python3.6+

## Changelog

[Here](docs/CHANGELOG.md)

## License

[MIT](docs/LICENSE)

## Credits

This package was created with [cookiecutter](https://github.com/audreyr/cookiecutter) and [iamgodot/gen-pyckage](https://github.com/iamgodot/gen-pyckage) project template.
