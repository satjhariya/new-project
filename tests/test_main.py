import logging

from new_project.core import get_logger, get_settings, shutdown_logging


def test_logger_uses_configured_log_level(monkeypatch):
    monkeypatch.setenv("DEFAULT_LOG_LEVEL", "DEBUG")
    get_settings.cache_clear()
    shutdown_logging()

    logger = get_logger("test")

    assert logger.isEnabledFor(logging.DEBUG)

    shutdown_logging()
    get_settings.cache_clear()
