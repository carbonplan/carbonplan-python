# flake8: noqa
try:
    from carbonplan_data import *
except ImportError as e:
    msg = (
        "CarbonPlan's Data package is not installed.\n\n"
        'Please install the carbonplan_data package:\n\n'
        '  python -m pip install "carbonplan_data"'
    )
    raise ImportError(msg) from e
