import pytest

from .dayX import exec


def test_read():
    test = exec()
    assert test
