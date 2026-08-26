from __future__ import annotations

import logging
import os
import sys
from typing import Final

from .config import get_settings

_CONFIGURED: bool = False

# Combined the cleaner pipe format with the detailed filename/funcName from logging2.py
_DEFAULT_FORMAT: Final[str] = (
    "%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(funcName)s() | %(message)s"
)
_DEFAULT_DATEFMT: Final[str] = "%Y-%m-%d %H:%M:%S"


def configure_logging(
    level: str | int = "INFO",
    log_file: str | None = None,
    use_stderr: bool = False,
) -> None:
    """
    Configure application logging for both console and optionally a file.

    This function is safe to call multiple times. Calling it again
    will reconfigure the logging system, clearing old handlers.
    """
    global _CONFIGURED

    if isinstance(level, str):
        level = level.upper()
        if not hasattr(logging, level):
            raise ValueError(f"Unknown log level: {level}")
        level = getattr(logging, level)

    # Log to stdout or stderr depending on the application's stdio mode.
    stream = sys.stderr if use_stderr else sys.stdout
    handlers: list[logging.Handler] = [logging.StreamHandler(stream)]

    # Add file handler if requested (creating directories if needed)
    if log_file:
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        handlers.append(logging.FileHandler(log_file))

    # basicConfig with force=True will clear any existing handlers on the root logger
    logging.basicConfig(
        level=level,
        format=_DEFAULT_FORMAT,
        datefmt=_DEFAULT_DATEFMT,
        handlers=handlers,
        force=True,
    )

    _CONFIGURED = True


def get_logger(name: str) -> logging.Logger:
    """
    Return a named logger.

    Logging is configured automatically with defaults if it has not
    already been initialized.
    """
    if not _CONFIGURED:
        configure_logging(level=get_settings().default_log_level)

    return logging.getLogger(name)


def shutdown_logging() -> None:
    """
    Flush and close all logging handlers.
    """
    global _CONFIGURED
    logging.shutdown()
    _CONFIGURED = False
