# New Python Project

A Python project template with modern development best practices.

## Features

- 🐍 Python 3.9+ support
- 📦 Modern packaging with `pyproject.toml`
- 🧪 Testing with pytest
- 🔧 Code formatting with Black and isort
- 📏 Linting with flake8 and mypy
- 🔒 Pre-commit hooks for code quality
- 📚 Documentation ready
- 🌍 Environment management

## Quick Start

### Prerequisites

- Python 3.9 or higher
- Git

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd new-python-project
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Or install just production dependencies
pip install -r requirements.txt
```

4. Set up pre-commit hooks (optional but recommended):
```bash
pre-commit install
```

5. Copy environment template and configure:
```bash
cp .env.template .env
# Edit .env file with your configuration
```

## Development

### Project Structure

```
new-python-project/
├── src/                    # Source code
│   └── new_python_project/ # Main package
├── tests/                  # Test files
├── docs/                   # Documentation
├── scripts/                # Utility scripts
├── config/                 # Configuration files
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
├── pyproject.toml          # Project configuration
├── .gitignore             # Git ignore rules
├── .env.template          # Environment template
└── README.md              # This file
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test
pytest tests/test_example.py
```

### Code Quality

```bash
# Format code
black src tests

# Sort imports
isort src tests

# Lint code
flake8 src tests

# Type checking
mypy src
```

### Installing the Package

```bash
# Development installation
pip install -e .

# With development dependencies
pip install -e ".[dev]"
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and ensure code quality
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
