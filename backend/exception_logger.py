from datetime import datetime
from logging import error
from pprint import pformat


def log_exception(msg: str, ex: Exception = None) -> None:
    """Logs exception as error, formatting ex.args object"""

    error(f"{datetime.now().isoformat(sep=' ', timespec='milliseconds')}\t{msg}\t{pformat(ex.args, indent=4)}")
