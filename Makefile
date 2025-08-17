.PHONY: run lint format type test cov

run:
	poetry run fastapi dev app/main.py

lint:
	poetry run black --check .
	poetry run ruff check .
	poetry run mypy .

format:
	poetry run black .
	poetry run ruff check --fix .

format-check:
	poetry run black --check .
	poetry run ruff check .

pre-commit:
	poetry run pre-commit run --all-files

type:
	poetry run mypy .

test:
	cp .env .env-copy
	cp devtools/envs/.env.test .env
	poetry run pytest
	cp .env-copy .env
	rm -f .env-copy

cov:
	poetry run coverage run -m pytest
	poetry run coverage report -m

cov-html:
	poetry run coverage run -m pytest
	poetry run coverage html

help:
	@echo "make commit m='sua mensagem' (tipos: feat, fix, docs, style, refactor, test, chore, revert)"

commit:
	chmod +x ./devtools/git-commit.sh
	./devtools/git-commit.sh $(m)
