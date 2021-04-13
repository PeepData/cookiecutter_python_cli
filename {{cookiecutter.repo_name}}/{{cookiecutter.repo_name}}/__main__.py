import logging
import os
import sys
from logging.config import fileConfig

import click

if not os.path.exists("logs"):
    os.makedirs("logs")

from {{cookiecutter.repo_name}} import settings
from {{cookiecutter.repo_name}}.services import ExampleService


@click.group()
def cli():
    """Description about the project."""
    logging.config.fileConfig(settings.LOG_CONFIG)


@click.command()
def run():
    """Run project."""
    logging.info("El proceso ha comenzado.")
    ExampleService.example_function()
    logging.info("El proceso ha finalizado.")


cli.add_command(run)

if __name__ == "__main__":
    cli()
