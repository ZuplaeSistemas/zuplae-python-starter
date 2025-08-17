import pytest
from unittest.mock import Mock
from pytest_mock import MockerFixture
from app.domains.health.use_case import HealthUseCase


@pytest.mark.usefixtures("mocker")
class TestHealthUseCase:
    @pytest.fixture(autouse=True)
    def _setup(self, mocker: MockerFixture) -> None:
        """Executa antes de cada teste da classe"""
        self.repo: Mock = mocker.Mock()

    def test_execute_returns_true(self) -> None:
        self.repo.ready.return_value = True
        uc = HealthUseCase(self.repo)

        result: bool = uc.execute()

        assert result is True
        self.repo.ready.assert_called_once()

    def test_execute_returns_false(self) -> None:
        self.repo.ready.return_value = False
        uc = HealthUseCase(self.repo)

        result: bool = uc.execute()

        assert result is False
        self.repo.ready.assert_called_once()
