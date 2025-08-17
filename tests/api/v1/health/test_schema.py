import pytest
from pydantic import ValidationError
from app.api.v1.health.schema import HealthResponse


class TestHealthSchema:
    def test_valid_schema(self) -> None:
        data: dict[str, str] = {"status": "ok", "service": "zuplae-python-starter"}
        health_response = HealthResponse(**data)
        assert health_response.status == "ok"
        assert health_response.service == "zuplae-python-starter"

    def test_invalid_status_raises_error(self) -> None:
        data = {"status": 123, "service": "zuplae-python-starter"}
        with pytest.raises(ValidationError):
            HealthResponse(**data)

    def test_missing_field_raises_error(self) -> None:
        data = {"status": "ok"}
        with pytest.raises(ValidationError):
            HealthResponse(**data)
