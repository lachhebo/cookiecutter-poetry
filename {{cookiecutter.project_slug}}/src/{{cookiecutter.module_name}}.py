"""Main module."""

from importlib.metadata import version


def main():
    return version('pytest')