# flake8: noqa
try:
    from carbonplan_forests import *
except ImportError as e:
    msg = (
        "CarbonPlan's Forests package is not installed.\n\n"
        'Please install the carbonplan-forests package:\n\n'
        '  python -m pip install "carbonplan-forests"'
    )
    raise ImportError(msg) from e
