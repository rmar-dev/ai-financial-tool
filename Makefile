# Makefile for ai-financial-tool

.PHONY: help install install-dev test lint format type-check clean docs

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install production dependencies
	pip install -r requirements.txt

install-dev:  ## Install development dependencies
	pip install -r requirements-dev.txt
	pre-commit install

test:  ## Run tests
	pytest

test-cov:  ## Run tests with coverage
	pytest --cov=src --cov-report=html --cov-report=term

lint:  ## Run all linting tools
	flake8 src tests
	mypy src

format:  ## Format code with black and isort
	black src tests
	isort src tests

format-check:  ## Check code formatting without making changes
	black --check src tests
	isort --check-only src tests

type-check:  ## Run type checking
	mypy src

clean:  ## Clean up generated files
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

docs:  ## Generate documentation
	@echo "Documentation generation not yet configured"

build:  ## Build the package
	python -m build

install-package:  ## Install the package in development mode
	pip install -e .

install-package-dev:  ## Install the package with dev dependencies
	pip install -e ".[dev]"

all-checks: format-check lint type-check test  ## Run all quality checks
