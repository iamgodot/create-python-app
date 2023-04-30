from os import remove
from os.path import join

MODULE_NAME = "{{ cookiecutter.project_slug }}"

if "no" in "{{ cookiecutter.cli_framework|lower }}":
    remove(join("src", MODULE_NAME, "cli.py"))

print(f"Project {MODULE_NAME} created successfully.")
