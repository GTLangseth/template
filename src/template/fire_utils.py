#!/usr/env/bin python3

"""Fire utils for interacting with CLI Module."""

# built in libs
import functools
from typing import Any, Callable

# external libs
import fire


def bonfire(obj: Callable[..., Any]) -> Callable[..., Any]:
    """Wrapper utility for fire.Fire.

    Simple wrapper function to wrap python object
    with the fire decorator. Note that any args and kwargs
    are ignored in favor of those passed from command line.

    Option to make more complex in future implementations,
    adding overrides to parsing of commands from `sys.argv`

    Args:
        obj: The function or class object to get transformed to CLI tool.

    Returns:
        A function wrapped in fire.Fire wrapper
    """

    @functools.wraps(obj)
    def fire_wrapper(*args: Any, **kwargs: Any) -> None:
        fire.Fire(obj)
        return None

    return fire_wrapper
