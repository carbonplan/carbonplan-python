# flake8: noqa
try:
    from carbonplan_trace import *
except ImportError as e:
    msg = (
        "CarbonPlan's Trace package is not installed.\n\n"
        'Please install the carbonplan-trace package:\n\n'
        '  python -m pip install "carbonplan-trace"'
    )
    raise ImportError(msg) from e
