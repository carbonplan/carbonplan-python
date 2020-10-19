# flake8: noqa
try:
    from carbonplan_styles import *
except ImportError as e:
    msg = (
        "CarbonPlan's Styles package is not installed.\n\n"
        'Please install the carbonplan-styles package:\n\n'
        '  python -m pip install "carbonplan-styles"'
    )
    raise ImportError(msg) from e
