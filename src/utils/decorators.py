from typing import Callable
import time
from functools import wraps
import logging


def _func_full_name(func: Callable) -> str:
    """Retrieve full function name

    Args:
        func: callable to pull metadata from

    Returns:
        func name
    """
    if not getattr(func, "__module__", None):
        return getattr(func, "__qualname__", repr(func))
    return f"{func.__module__}.{func.__qualname__}"


def _human_readable_time(elapsed: float) -> str:
    """Convert elapsed seconds to readable time

    Args:
        elapsed: elapsed time in seconds

    Returns:
        Readable time
    """
    mins, secs = divmod(elapsed, 60)
    hours, mins = divmod(mins, 60)

    if hours > 0:
        message = "%dh%02dm%02ds" % (hours, mins, secs)
    elif mins > 0:
        message = "%dm%02ds" % (mins, secs)
    elif secs >= 1:
        message = f"{secs:.2f}"
    else:
        message = f"{secs * 1000.0:.0f}ms"
    return message


def log_time(func: Callable) -> Callable:
    """A function decorator which logs time taken to execute a function
    Args:
        func: The function to be logged

    Returns:
        A wrapped function which will execute the provided function and log the
        running time.
    """

    @wraps(func)
    def with_time(*args, **kwargs):
        logger = logging.getLogger(__name__)
        t_start = time.time()
        result = func(*args, **kwargs)
        t_end = time.time()
        elapsed = t_end - t_start

        logger.info(
            "Running %r took %s [%.3fs]",
            _func_full_name(func),
            _human_readable_time(elapsed),
            elapsed,
        )

        return result

    return with_time
