# flake8: noqa
try:
    from carbonplan_forest_offsets import *
except ImportError as e:
    msg = (
        "CarbonPlan's Forests Offsets package is not installed.\n\n"
        'Please install the carbonplan-forest-offsets package:\n\n'
        '  python -m pip install "carbonplan-forest-risks"'
    )
    raise ImportError(msg) from e
