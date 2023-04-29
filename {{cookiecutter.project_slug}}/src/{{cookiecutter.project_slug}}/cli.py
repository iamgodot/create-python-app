{% if cookiecutter.cli_framework|lower == 'click' -%}
import click


@click.command()
def main():
    click.echo("This is {{ cookiecutter.project_slug }} CLI.")
{%- endif %}
