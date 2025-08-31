# Installation Guide

This guide covers different ways to install and set up the New Python Project.

## System Requirements

- **Python**: 3.9 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: 512MB RAM minimum
- **Storage**: 100MB free space

## Installation Methods

### Method 1: Development Installation (Recommended)

This is the recommended method if you plan to contribute or modify the code.

```bash
# 1. Clone the repository
git clone <repository-url>
cd new-python-project

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows Command Prompt
.\venv\Scripts\activate.bat

# macOS/Linux
source venv/bin/activate

# 4. Upgrade pip
python -m pip install --upgrade pip

# 5. Install development dependencies
pip install -r requirements-dev.txt

# 6. Install package in development mode
pip install -e .

# 7. Set up pre-commit hooks (optional but recommended)
pre-commit install
```

### Method 2: Production Installation

For production use or if you just want to use the package:

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\Activate.ps1  # Windows

# 3. Install from PyPI (when published)
pip install new-python-project

# OR install from source
pip install git+<repository-url>
```

### Method 3: User Installation

Install for the current user only:

```bash
pip install --user new-python-project
```

## Verification

After installation, verify everything works:

### 1. Test the Installation

```bash
# Check if the package is importable
python -c "import new_python_project; print('Installation successful!')"

# Run the main application
python -m new_python_project.main
# OR
python src/new_python_project/main.py
```

### 2. Run Tests (Development Installation)

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Expected output: All tests should pass
```

### 3. Check Development Tools (Development Installation)

```bash
# Check code formatting
black --check src tests

# Check import sorting
isort --check-only src tests

# Check linting
flake8 src tests

# Check type annotations
mypy src

# Or run all checks
python scripts/dev.py all
```

## IDE Setup

### Visual Studio Code

1. **Install VS Code** (if not already installed):
   ```bash
   winget install Microsoft.VisualStudioCode
   ```

2. **Open the project**:
   ```bash
   code .
   ```

3. **Recommended Extensions**:
   - Python (ms-python.python)
   - Pylance (ms-python.vscode-pylance)
   - Python Debugger (ms-python.debugpy)
   - Black Formatter (ms-python.black-formatter)
   - isort (ms-python.isort)
   - GitLens (eamodio.gitlens)

4. **VS Code will automatically**:
   - Detect your virtual environment
   - Configure the Python interpreter
   - Enable debugging and testing

### PyCharm

1. Open the project directory in PyCharm
2. Configure Python interpreter to use `venv/Scripts/python.exe`
3. Enable pytest as the test runner
4. Configure Black as the code formatter

## Environment Configuration

### 1. Create Environment File

```bash
# Copy the template
cp .env.template .env

# Edit with your values
# Windows
notepad .env

# macOS/Linux
nano .env
```

### 2. Common Environment Variables

```env
# Application settings
APP_NAME=new-python-project
APP_VERSION=0.1.0
DEBUG=True
LOG_LEVEL=INFO

# Database (if using)
DATABASE_URL=sqlite:///./app.db

# API keys (if using external services)
API_KEY=your_api_key_here
```

## Troubleshooting

### Common Issues

#### Virtual Environment Not Activating

**Windows PowerShell Execution Policy**:
```powershell
# Check current policy
Get-ExecutionPolicy

# Set policy for current user (if needed)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Import Errors

```bash
# Make sure you're in the virtual environment
# You should see (venv) in your prompt

# Reinstall the package
pip install -e .

# Check if the package is in the Python path
python -c "import sys; print('\n'.join(sys.path))"
```

#### Test Failures

```bash
# Run tests in verbose mode
pytest -v

# Run a specific test
pytest tests/test_main.py::test_greet_with_name -v

# Check test coverage
pytest --cov=src --cov-report=html
# Then open htmlcov/index.html
```

#### Pre-commit Hook Failures

```bash
# Run pre-commit manually
pre-commit run --all-files

# Update pre-commit hooks
pre-commit autoupdate

# Skip hooks temporarily (not recommended)
git commit --no-verify
```

### Getting Help

If you encounter issues:

1. Check this troubleshooting section
2. Look at the [FAQ](faq.md)
3. Review the error messages carefully
4. Check that all prerequisites are met
5. Ensure you're using a supported Python version

### System-Specific Notes

#### Windows
- Use PowerShell or Command Prompt
- Make sure Windows Defender doesn't block the virtual environment
- Some corporate environments may restrict script execution

#### macOS
- You may need to install Xcode command line tools
- Use `python3` instead of `python` if needed

#### Linux
- Install `python3-venv` if virtual environment creation fails
- Some distributions require `python3-dev` for certain packages

## What's Next?

After successful installation:

1. Read the [Development Guide](development.md)
2. Explore the [Examples](../examples/index.md)
3. Check out the [API Reference](../api/index.md)
4. Start building your application!
