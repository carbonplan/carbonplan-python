import importlib

import pytest


@pytest.mark.parametrize(
    'mod',
    [
        'carbonplan',
        'carbonplan.data',
        'carbonplan.styles',
    ],
)
def test_import_submodules(mod):
    mod = importlib.import_module(mod)
    assert mod.version
