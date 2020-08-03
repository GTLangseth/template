#!/usr/env/bin python

# Docs configuration file

"""Sphinx configuration."""
project = "template"
author = "Grant Langseth"
copyright = f"2020, {author}"


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]
