import re
import sys

MODULE_REGEX = r'^[a-zA-Z][_a-zA-Z0-9]+$'
MODULE_NAME = '{{ cookiecutter.project_slug }}'

if not re.match(MODULE_REGEX, MODULE_NAME):
    print(f'ERROR: {MODULE_NAME} is not a valid Python module name!')
    sys.exit(1)
