import logging
from pathlib import Path

from new_project.core import configure_logging, get_logger, get_settings, shutdown_logging


def test_logger_uses_configured_log_level(monkeypatch):
    monkeypatch.setenv("DEFAULT_LOG_LEVEL", "DEBUG")
    get_settings.cache_clear()
    shutdown_logging()

    logger = get_logger("test")

    assert logger.isEnabledFor(logging.DEBUG)

    shutdown_logging()
    get_settings.cache_clear()


def test_logger_writes_to_configured_file(tmp_path, monkeypatch):
    log_path = tmp_path / "logs" / "app.log"
    monkeypatch.setenv("LOG_FILE", str(log_path))
    get_settings.cache_clear()
    shutdown_logging()

    configure_logging(log_file=str(log_path))
    get_logger("test").info("file log")
    shutdown_logging()

    assert Path(log_path).is_file()
    assert "file log" in log_path.read_text()
    get_settings.cache_clear()
