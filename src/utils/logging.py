import logging
from typing import Optional, Union
import colorlog


def configure_logging(
    log_file: Optional[Union[str, "Path"]] = None,
    debug: bool = False,
    logger: Optional["logging.Logger"] = None,
) -> None:
    """Configure logging

    >>> Add color stream handler
    >>> set logging verbosity
    >>> add log file

    Args:
        log_file: optional file to send logs to.
        debug: if running in debug mode
        logger: optional __main__ logger to set.

    Returns:
        None.
    """
    _base_format = "[%(levelname)s] | %(asctime)s | %(name)s | %(message)s"

    # set handlers
    sh = logging.StreamHandler()
    colour_format = colorlog.ColoredFormatter(
        fmt="%(log_color)s[%(levelname)s]%(reset)s | %(name)s | %(message)s"
    )
    sh.setFormatter(colour_format)
    handlers = [sh]

    if log_file is not None:
        fh = logging.FileHandler(log_file, encoding="utf-8")
        formatter = logging.Formatter(fmt=_base_format)
        fh.setFormatter(formatter)
        handlers.append(fh)

    # set level
    if debug:
        level = logging.DEBUG
    else:
        level = logging.INFO

    # configure
    logging.basicConfig(format=_base_format, handlers=handlers)
    library_root_logger = _get_root_logger()
    library_root_logger.setLevel(level=level)

    if logger is not None:
        logger.setLevel(level=level)

    return None


def _get_root_logger() -> logging.Logger:
    return logging.getLogger(_get_library_name())


def _get_library_name() -> str:
    return __name__.split(".")[0]
