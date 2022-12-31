#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""src/run.py

This is the main entry point for the {{ cookiecutter.package_name }} package.

Usage: python run.py --name <name> --position <position> --start_date <start_date>
___
--help       | -h Display documentation
--name       | -n Name of the person
--position   | -p Position within the company
--start_date | -s First day of work
"""

import click


# Function example declaration
def hello_world(my_name: str, my_position: str, my_start_date: str) -> str:
    """Say hello to world!

    Arguments:
        my_name (str) -- Name of the person
        my_position (str) -- Position within the company
        my_start_date (str) -- First day of work

    Returns:
        str -- Greeting message
    """
    return f"Hello World! I'm {my_name} and I'm a {my_position} since {my_start_date}."


# Click command example
@click.command()
@click.option("--name", default="John Doe", help="Name of the person")
@click.option(
    "--position", default="Software Engineer", help="Position within the company"
)
@click.option("--start_date", default="2020-01-01", help="First day of work")
def main(name: str, position: str, start_date: str):
    """Main function"""
    print(hello_world(name, position, start_date))


if __name__ == "__main__":
    main()
