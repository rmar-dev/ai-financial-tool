"""Tests for the main module."""

import pytest

from new_python_project.main import greet, setup_logging


def test_greet_with_name() -> None:
    """Test greeting with a specific name."""
    result = greet("Alice")
    assert result == "Hello, Alice!"


def test_greet_without_name() -> None:
    """Test greeting without a name."""
    result = greet()
    assert result == "Hello, World!"


def test_greet_with_none() -> None:
    """Test greeting with None as name."""
    result = greet(None)
    assert result == "Hello, World!"


def test_greet_with_empty_string() -> None:
    """Test greeting with empty string."""
    result = greet("")
    assert result == "Hello, World!"


def test_setup_logging() -> None:
    """Test that setup_logging doesn't raise an exception."""
    # This test ensures the function can be called without errors
    setup_logging("INFO")
    setup_logging("DEBUG")
    setup_logging("WARNING")


class TestGreetParameterized:
    """Parametrized tests for the greet function."""

    @pytest.mark.parametrize(
        "name,expected",
        [
            ("Bob", "Hello, Bob!"),
            ("Charlie", "Hello, Charlie!"),
        ],
    )
    def test_greet_parametrized(self, name: str, expected: str) -> None:
        """Test greet function with various inputs."""
        result = greet(name)
        assert result == expected
