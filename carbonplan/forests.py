# flake8: noqa
try:
    from carbonplan_forests import *
except ImportError as e:
    msg = (
        "CarbonPlan's Forests package is not installed.\n\n"
        'Please install the carbonplan_forests package:\n\n'
        '  python -m pip install "carbonplan_forests"'
    )
    raise ImportError(msg) from e
