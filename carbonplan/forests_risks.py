# flake8: noqa
try:
    from carbonplan_forest_risks import *
except ImportError as e:
    msg = (
        "CarbonPlan's Forests Risks package is not installed.\n\n"
        'Please install the carbonplan-forests package:\n\n'
        '  python -m pip install "carbonplan-forest-risks"'
    )
    raise ImportError(msg) from e
