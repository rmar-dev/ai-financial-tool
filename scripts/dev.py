#!/usr/bin/env python3
"""Development script for common tasks."""

import argparse
import subprocess
import sys


def run_command(command: str, description: str) -> bool:
    """Run a shell command and return success status."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True
        )
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False


def format_code() -> bool:
    """Format code with black and isort."""
    success = True
    success &= run_command("black src tests", "Formatting with Black")
    success &= run_command("isort src tests", "Sorting imports with isort")
    return success


def lint_code() -> bool:
    """Run linting tools."""
    success = True
    success &= run_command("flake8 src tests", "Linting with flake8")
    success &= run_command("mypy src", "Type checking with mypy")
    return success


def run_tests() -> bool:
    """Run tests with coverage."""
    return run_command(
        "pytest --cov=src --cov-report=term", "Running tests with coverage"
    )


def main() -> None:
    """Run the main entry point."""
    parser = argparse.ArgumentParser(description="Development tools for the project")
    parser.add_argument(
        "command",
        choices=["format", "lint", "test", "all"],
        help="Command to run",
    )

    args = parser.parse_args()

    success = True

    if args.command == "format":
        success = format_code()
    elif args.command == "lint":
        success = lint_code()
    elif args.command == "test":
        success = run_tests()
    elif args.command == "all":
        print("🚀 Running all development checks...")
        success &= format_code()
        success &= lint_code()
        success &= run_tests()

        if success:
            print("🎉 All checks passed!")
        else:
            print("💥 Some checks failed!")

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
