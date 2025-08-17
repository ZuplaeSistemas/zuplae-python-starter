from app.domains.health.repository import HealthRepository


class HealthUseCase:
    def __init__(self, repo: HealthRepository) -> None:
        self.repo = repo

    def execute(self) -> bool:
        return self.repo.ready()
