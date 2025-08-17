import pytest
from httpx import AsyncClient
from pytest_mock import MockerFixture
from app.main import app
from app.domains.health.use_case import HealthUseCase
from app.core import deps


class TestHealthController:
    @pytest.mark.asyncio
    async def test_liveness(self, client: AsyncClient) -> None:
        response = await client.get("/api/v1/health/liveness")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["service"] == "zuplae-python-starter"

    @pytest.mark.asyncio
    async def test_readiness_ok(
        self, client: AsyncClient, mocker: MockerFixture
    ) -> None:
        uc_mock = mocker.Mock(spec=HealthUseCase)
        uc_mock.execute.return_value = True

        app.dependency_overrides[deps.get_check_health] = lambda: uc_mock

        response = await client.get("/api/v1/health/readiness")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["service"] == "zuplae-python-starter"
        uc_mock.execute.assert_called_once()

        app.dependency_overrides.clear()

    @pytest.mark.asyncio
    async def test_readiness_degraded(
        self, client: AsyncClient, mocker: MockerFixture
    ) -> None:
        uc_mock = mocker.Mock(spec=HealthUseCase)
        uc_mock.execute.return_value = False

        app.dependency_overrides[deps.get_check_health] = lambda: uc_mock

        response = await client.get("/api/v1/health/readiness")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "degraded"
        assert data["service"] == "zuplae-python-starter"
        uc_mock.execute.assert_called_once()

        app.dependency_overrides.clear()
