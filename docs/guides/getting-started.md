# Getting Started

This guide will help you get up and running with the New Python Project quickly.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9 or higher**
- **Git** (for version control)
- **Visual Studio Code** (recommended IDE)

## Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd new-python-project

# Create and activate virtual environment
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies

```bash
# Install development dependencies (recommended)
pip install -r requirements-dev.txt

# Or install just production dependencies
pip install -r requirements.txt
```

### 3. Install the Package

```bash
# Install in development mode
pip install -e .
```

### 4. Verify Installation

```bash
# Run the sample application
python src\new_python_project\main.py

# Run tests
pytest

# Check code quality
python scripts\dev.py all
```

## Your First Steps

### 1. Explore the Code

The main application code is in `src/new_python_project/main.py`. Take a look at:

- The `greet()` function - a simple example with type hints
- The `setup_logging()` function - logging configuration
- The `main()` function - application entry point

### 2. Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_main.py
```

### 3. Try the Development Tools

```bash
# Format your code
black src tests

# Sort imports
isort src tests

# Check for linting issues
flake8 src tests

# Run type checking
mypy src

# Or run all checks at once
python scripts\dev.py all
```

### 4. Make Your First Changes

1. Edit `src/new_python_project/main.py`
2. Add a new function
3. Write tests for it in `tests/`
4. Run the quality checks
5. Commit your changes

## Project Structure Explained

```
new-python-project/
├── src/                     # Source code
│   └── new_python_project/  # Main package
│       ├── __init__.py      # Package initialization
│       └── main.py          # Main application module
├── tests/                   # Test files
│   ├── __init__.py          # Test package initialization
│   └── test_main.py         # Tests for main module
├── docs/                    # Documentation
├── scripts/                 # Development utilities
│   └── dev.py               # Development task runner
├── config/                  # Configuration files
├── .env.template            # Environment variables template
├── .gitignore              # Git ignore rules
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── pyproject.toml          # Modern Python project configuration
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
└── README.md               # Project overview
```

## Configuration

### Environment Variables

1. Copy the environment template:
   ```bash
   cp .env.template .env
   ```

2. Edit `.env` with your specific configuration:
   ```env
   APP_NAME=new-python-project
   DEBUG=True
   LOG_LEVEL=INFO
   ```

### Development Tools Configuration

All development tools are pre-configured in `pyproject.toml`:

- **Black**: Code formatting (88 character line length)
- **isort**: Import sorting (compatible with Black)
- **flake8**: Linting (configured in `.flake8`)
- **mypy**: Type checking
- **pytest**: Testing framework

## Next Steps

- Read the [Development Guide](development.md) to learn about the development workflow
- Check out the [API Reference](../api/index.md) for detailed code documentation
- Look at [Examples](../examples/index.md) for usage patterns
- Review the [FAQ](faq.md) for common questions

## Need Help?

- Check the [troubleshooting section](troubleshooting.md)
- Review the [FAQ](faq.md)
- Look at the existing tests for examples
- Read the inline code documentation
