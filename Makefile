# Run the fingraphrag example with the same inputs documented in the quickstart.
.PHONY: dev test lint

dev:
	python fingraphrag.py "Northwind" --mode hybrid

test:
	python -m pytest --cov=fingraphrag --cov-fail-under=70

lint:
	ruff check .
	ruff format --check .
	mypy fingraphrag.py
