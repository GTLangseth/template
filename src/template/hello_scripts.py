#!/usr/env/bin python

"""Template Script Specification File."""

from template.fire_utils import bonfire
from template.hello import Hello, hello


# script to interact with hello-fire
hello_bonfire = bonfire(hello)

# script to interact with hello-fire class
hello_class = bonfire(Hello)
