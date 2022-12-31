#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""tests/test_run.py

A single example test file for the {{ cookiecutter.package_name }} package.
"""

from {{cookiecutter.package_name}}.run import test_hello_world


def test_hello_world():
    """Test function for hello_world"""
    assert (
        hello_world("John Doe", "Software Engineer", "2020-01-01")
        == "Hello World! I'm John Doe and I'm a Software Engineer since 2020-01-01."
    )
