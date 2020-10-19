import importlib

import pytest


@pytest.mark.parametrize(
    'mod', ['carbonplan', 'carbonplan.data', 'carbonplan.forests', 'carbonplan.styles']
)
def test_import_submodules(mod):
    assert importlib.import_module(mod)
