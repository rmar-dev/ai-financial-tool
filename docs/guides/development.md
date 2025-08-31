# Development Guide

This guide covers the development workflow, coding standards, and best practices for contributing to the New Python Project.

## Development Workflow

### 1. Setting Up Your Development Environment

```bash
# Clone and enter the project
git clone <repository-url>
cd new-python-project

# Set up virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # macOS/Linux

# Install development dependencies
pip install -r requirements-dev.txt
pip install -e .

# Set up pre-commit hooks
pre-commit install
```

### 2. Development Cycle

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Write your code**:
   - Add functionality in `src/new_python_project/`
   - Write tests in `tests/`
   - Update documentation if needed

3. **Run quality checks**:
   ```bash
   python scripts/dev.py all
   ```

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add your feature description"
   ```

5. **Push and create pull request**:
   ```bash
   git push origin feature/your-feature-name
   ```

## Coding Standards

### Python Style Guide

We follow **PEP 8** with some modifications:

- **Line length**: 88 characters (Black default)
- **Import sorting**: isort with Black profile
- **Type hints**: Required for all public functions
- **Docstrings**: Google style docstrings

### Code Formatting

We use **Black** for automatic code formatting:

```bash
# Format all code
black src tests

# Check formatting without changes
black --check src tests
```

### Import Sorting

We use **isort** for consistent import ordering:

```bash
# Sort imports
isort src tests

# Check import sorting
isort --check-only src tests
```

### Type Checking

We use **mypy** for static type checking:

```bash
# Run type checking
mypy src

# Type checking configuration is in pyproject.toml
```

### Linting

We use **flake8** for code linting:

```bash
# Run linting
flake8 src tests

# Configuration is in .flake8
```

## Testing Guidelines

### Writing Tests

1. **Test file naming**: `test_*.py`
2. **Test function naming**: `test_*`
3. **Test class naming**: `Test*`

### Test Structure

```python
"""Tests for the example module."""

import pytest
from new_python_project.example import example_function


def test_example_function_with_valid_input():
    """Test example function with valid input."""
    # Arrange
    input_value = "test"
    expected = "expected_result"

    # Act
    result = example_function(input_value)

    # Assert
    assert result == expected


class TestExampleClass:
    """Tests for ExampleClass."""

    def test_method(self):
        """Test a specific method."""
        # Test implementation
        pass
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_main.py

# Run specific test function
pytest tests/test_main.py::test_greet_with_name

# Run tests matching a pattern
pytest -k "greet"

# Run tests with verbose output
pytest -v
```

### Test Coverage

We aim for **80%+ test coverage**:

```bash
# Generate coverage report
pytest --cov=src --cov-report=html

# View coverage report
# Open htmlcov/index.html in your browser
```

## Documentation

### Writing Documentation

1. **API Documentation**: Use docstrings in Google style
2. **Guides**: Write in Markdown in `docs/guides/`
3. **Examples**: Add code examples in `docs/examples/`

### Docstring Style

```python
def example_function(param1: str, param2: int = 0) -> str:
    """Brief description of the function.

    Longer description if needed. This can span multiple lines
    and provide detailed information about the function's behavior.

    Args:
        param1: Description of the first parameter.
        param2: Description of the second parameter. Defaults to 0.

    Returns:
        Description of what the function returns.

    Raises:
        ValueError: Description of when this exception is raised.
        TypeError: Description of when this exception is raised.

    Example:
        Basic usage example:

        >>> result = example_function("hello", 42)
        >>> print(result)
        'hello42'
    """
    return f"{param1}{param2}"
```

### Building Documentation

```bash
# Build Sphinx documentation
cd docs
sphinx-build -b html source build

# Build MkDocs documentation
mkdocs build

# Serve documentation locally
mkdocs serve
```

## Code Quality Tools

### Pre-commit Hooks

Pre-commit hooks run automatically before each commit:

```bash
# Install hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files

# Update hooks
pre-commit autoupdate
```

### Development Script

Use the development script for common tasks:

```bash
# Run all quality checks
python scripts/dev.py all

# Just format code
python scripts/dev.py format

# Just run linting
python scripts/dev.py lint

# Just run tests
python scripts/dev.py test
```

### Makefile Commands

Alternatively, use Makefile commands:

```bash
# Show available commands
make help

# Install development dependencies
make install-dev

# Run tests with coverage
make test-cov

# Format code
make format

# Run all quality checks
make all-checks
```

## Adding New Features

### 1. Adding a New Module

1. Create the module file in `src/new_python_project/`
2. Add proper docstrings and type hints
3. Create corresponding test file in `tests/`
4. Update `__init__.py` if needed
5. Add documentation

Example structure:
```
src/new_python_project/
├── __init__.py
├── main.py
└── utils.py        # New module

tests/
├── __init__.py
├── test_main.py
└── test_utils.py   # New test file
```

### 2. Adding Dependencies

1. **Production dependencies**: Add to `requirements.txt`
2. **Development dependencies**: Add to `requirements-dev.txt`
3. **Optional dependencies**: Add to `pyproject.toml` under `[project.optional-dependencies]`

### 3. Adding Configuration

1. Add new variables to `.env.template`
2. Document the variables
3. Update configuration loading code
4. Add tests for configuration

## Git Workflow

### Branch Naming

- **Features**: `feature/short-description`
- **Bug fixes**: `fix/short-description`
- **Documentation**: `docs/short-description`
- **Refactoring**: `refactor/short-description`

### Commit Messages

Follow conventional commit format:

```
type(scope): description

body (optional)

footer (optional)
```

Examples:
- `feat(auth): add user authentication`
- `fix(api): handle empty response correctly`
- `docs(readme): update installation instructions`
- `test(utils): add tests for helper functions`

### Pull Request Process

1. Create feature branch
2. Make your changes
3. Ensure all tests pass
4. Update documentation
5. Create pull request
6. Address review feedback
7. Merge after approval

## Performance Considerations

### Code Performance

1. **Profile your code** when needed:
   ```python
   import cProfile
   cProfile.run('your_function()')
   ```

2. **Use appropriate data structures**
3. **Avoid premature optimization**
4. **Write benchmarks for critical code**

### Testing Performance

```bash
# Run tests with timing
pytest --durations=10

# Run only fast tests
pytest -m "not slow"

# Run performance tests
pytest -m "performance"
```

## Security Guidelines

### 1. Environment Variables

- Never commit `.env` files
- Use `.env.template` for documentation
- Validate environment variables

### 2. Dependencies

- Regularly update dependencies
- Use `pip-audit` to check for vulnerabilities
- Pin dependency versions in production

### 3. Code Security

- Validate all inputs
- Use secure defaults
- Avoid eval() and exec()
- Be careful with file operations

## Release Process

### 1. Version Bumping

Update version in these files:
- `pyproject.toml`
- `src/new_python_project/__init__.py`

### 2. Changelog

Update `CHANGELOG.md` with:
- New features
- Bug fixes
- Breaking changes
- Migration notes

### 3. Release Steps

```bash
# 1. Create release branch
git checkout -b release/v1.0.0

# 2. Update version numbers
# Edit pyproject.toml and __init__.py

# 3. Update changelog
# Edit CHANGELOG.md

# 4. Run final quality checks
python scripts/dev.py all

# 5. Commit release changes
git commit -m "chore: bump version to 1.0.0"

# 6. Create and push tag
git tag v1.0.0
git push origin v1.0.0
```

## Debugging

### Using VS Code Debugger

1. Set breakpoints in your code
2. Use F5 to start debugging
3. Use the debug console to inspect variables

### Using Python Debugger

```python
# Add to your code for debugging
import pdb; pdb.set_trace()

# Or use breakpoint() (Python 3.7+)
breakpoint()
```

### Logging for Debugging

```python
import logging

logger = logging.getLogger(__name__)

def your_function():
    logger.debug("Debug information")
    logger.info("General information")
    logger.warning("Warning message")
    logger.error("Error message")
```

## Getting Help

- Read this development guide thoroughly
- Check the [API Reference](../api/index.md)
- Look at existing code for patterns
- Run tests to understand expected behavior
- Ask questions in issues or discussions
