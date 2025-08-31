"""Main module for the application."""

import logging
from typing import Optional


def setup_logging(level: str = "INFO") -> None:
    """Set up logging configuration.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def greet(name: Optional[str] = None) -> str:
    """Greet a person.

    Args:
        name: The name of the person to greet. If None or empty, greets everyone.

    Returns:
        A greeting message.
    """
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"


def main() -> None:
    """Run the main entry point of the application."""
    setup_logging()
    logger = logging.getLogger(__name__)

    logger.info("Starting application")
    message = greet("Developer")
    print(message)
    logger.info("Application finished")


if __name__ == "__main__":
    main()
