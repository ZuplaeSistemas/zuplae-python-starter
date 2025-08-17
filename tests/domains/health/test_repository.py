from app.domains.health.repository import InMemoryHealthRepository


class TestRepository:
    repo = InMemoryHealthRepository()

    def test_inmemory_health_repository_ready_true(self) -> None:
        assert self.repo.ready()
