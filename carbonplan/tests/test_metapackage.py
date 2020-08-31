import importlib


def test_import():
    module = importlib.import_module('carbonplan')
    assert module
