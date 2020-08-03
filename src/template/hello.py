#!/usr/env/bin python3

"""Template Hello Utility.

Just a simple hello-word like utility to expand and grow in complexity
alongside the complexity of the project.

Useful for verifying connectivity to various data connections and networked systems.
"""


def hello(name: str = "Covera") -> str:
    """Say hello to our little friend, 'name'.

    Args:
        name: The name to be greeted.

    Returns:
        A string with a nice greeting.

    Example:
        >>> from db_sync.hello import hello
        >>> response = hello("Doctor")
        >>> "Doctor" in response
        True
    """
    return f"Well hello there, {name}!"


class Hello:
    """This is a simple class used to say hello."""

    def __init__(self, name: str = "Covera") -> None:
        """Class initialized with name.

        Args:
            name: The name of the person to greet.
        """
        self.name = name

    def say_hello(self, name: str = None) -> str:
        """Call hello function on class name or new name."""
        name = name or self.name
        return hello(name)
