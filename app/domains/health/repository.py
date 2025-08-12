from typing import Protocol

class HealthRepository(Protocol):
    def ready(self) -> bool: ...

class InMemoryHealthRepository:
    def ready(self) -> bool:
        # Simples: sempre pronto. Substitua por checagens reais quando precisar.
        return True