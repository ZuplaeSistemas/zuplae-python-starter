import logging
import pytest
import io
from app.core import logging as core_logging


class TestLogging:
    def test_get_logger_returns_logger_instance(self) -> None:
        logger = core_logging.get_logger("app.test")
        assert isinstance(logger, logging.Logger)
        assert logger.name == "app.test"

    def test_setup_logging_configures_handlers(self) -> None:
        # roda a configuração
        core_logging.setup_logging()

        logger = core_logging.get_logger("app")

        # deve ter pelo menos 1 handler configurado
        assert logger.handlers, "Logger don't have any handlers configured"
        # o nível deve refletir o settings (default INFO)
        assert logger.level in (logging.INFO, logging.DEBUG, logging.WARNING)

    def test_logger_outputs_message(self, caplog: pytest.LogCaptureFixture) -> None:
        core_logging.setup_logging()
        logger = core_logging.get_logger("app")

        stream = io.StringIO()
        handler = logging.StreamHandler(stream)
        logger.addHandler(handler)

        logger.info("test message")
        handler.flush()

        output = stream.getvalue()
        assert "test message" in output
