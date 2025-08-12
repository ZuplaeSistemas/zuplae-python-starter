.PHONY: run lint format type test cov

run:
	poetry run fastapi dev app/main.py

lint:
	poetry run ruff check .

format:
	poetry run black .
	poetry run ruff check . --fix

type:
	poetry run mypy .

test:
	poetry run pytest -q

cov:
	poetry run coverage run -m pytest
	poetry run coverage html
	@echo "Abra htmlcov/index.html"