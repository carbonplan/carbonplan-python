# flake8: noqa
import warnings

try:
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', category=DeprecationWarning, module='intake')
        warnings.filterwarnings('ignore', category=PendingDeprecationWarning, module='intake')
        from carbonplan_data import *
except ImportError as e:
    msg = (
        "CarbonPlan's Data package is not installed.\n\n"
        'Please install the carbonplan-data package:\n\n'
        '  python -m pip install "carbonplan-data"'
    )
    raise ImportError(msg) from e
