#!/usr/env/bin python

"""Simple testing utility for template.hello."""

# import builtins
import subprocess

# import externals
import pytest
from pytest import fixture
from template import hello


@pytest.fixture(params=["Johnny", "Mikey"])
def input(request: fixture) -> str:
    """Simple function to return test data to hello script."""
    return request.param


def test_hello(input: fixture) -> None:
    """Check result is str and contains input."""
    result = hello.hello(input)
    assert type(result) is str
    assert input in result


def test_hello_bonfire(input: fixture) -> None:
    """Check output contains input."""
    result = subprocess.check_output(["hello", f"--name={input}"])
    assert bytes(input, "utf8") in result


def test_hello_class(input: fixture) -> None:
    """Check output contains input."""
    result = subprocess.check_output(["hello-class", "say_hello", f"--name={input}"])
    assert bytes(input, "utf8") in result
