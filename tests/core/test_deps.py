from app.core import deps
from app.domains.health.repository import InMemoryHealthRepository
from app.domains.health.use_case import HealthUseCase


class TestAppDeps:
    def test_get_health_repo_returns_inmemory_health_repository(self):
        repo = deps.get_health_repo()

        assert isinstance(repo, InMemoryHealthRepository)

    def test_get_check_health_returns_health_use_case(self):
        repo = InMemoryHealthRepository()
        uc = deps.get_check_health(repo)

        assert isinstance(uc, HealthUseCase)
        assert isinstance(uc.repo, InMemoryHealthRepository)
