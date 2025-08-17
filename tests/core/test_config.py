import importlib
import pytest

from app.core import config


class TestSettings:
    def test_default_settings(self) -> None:
        """Valida se os defaults do Settings estão corretos."""
        s = config.Settings()
        assert s.APP_NAME == "zuplae-python-starter"
        assert (
            s.APP_DESCRIPTION
            == "zuplae-python-starter com uma base moderna, rápida e padronizada — focada em FastAPI + Poetry, lint/format, testes, Docker e CI."
        )
        assert s.APP_VERSION == "0.0.1"
        assert s.API_PREFIX_V1 == "/api/v1"
        assert s.API_CORS_ORIGINS == ["http://localhost:3000", "http://127.0.0.1:3000"]
        assert s.LOG_LEVEL == "INFO"
        assert s.ENABLE_UVICORN_ACCESS_LOGS is True

    def test_env_override(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Simula variáveis de ambiente e garante que são lidas corretamente."""
        monkeypatch.setenv("APP_NAME", "custom-app")
        monkeypatch.setenv("LOG_LEVEL", "DEBUG")
        monkeypatch.setenv("ENABLE_UVICORN_ACCESS_LOGS", "false")
        monkeypatch.setenv(
            "API_CORS_ORIGINS", '["http://localhost", "https://zuplae.com"]'
        )

        # precisa recarregar o módulo para forçar reavaliação com novos envs
        import app.core.config as cfg

        importlib.reload(cfg)

        s = cfg.Settings()
        assert s.APP_NAME == "custom-app"
        assert s.LOG_LEVEL == "DEBUG"
        # valores booleanos são convertidos pelo Pydantic
        assert s.ENABLE_UVICORN_ACCESS_LOGS is False
        # listas em string JSON são parseadas
        assert "http://localhost" in s.API_CORS_ORIGINS
        assert "https://zuplae.com" in s.API_CORS_ORIGINS
