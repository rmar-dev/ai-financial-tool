"""Tests for the AI Financial Tool main module."""

from unittest.mock import Mock, patch

import pytest

from ai_financial_tool.main import FinancialAnalyzer, setup_logging


class TestFinancialAnalyzer:
    """Tests for the FinancialAnalyzer class."""

    def test_init(self) -> None:
        """Test FinancialAnalyzer initialization."""
        analyzer = FinancialAnalyzer()
        assert analyzer.data is None
        assert analyzer.logger is not None

    @patch("ai_financial_tool.main.yf")
    def test_fetch_stock_data_success(self, mock_yf: Mock) -> None:
        """Test successful stock data fetching."""
        # Mock yfinance
        mock_ticker = Mock()
        mock_data = Mock()
        mock_ticker.history.return_value = mock_data
        mock_yf.Ticker.return_value = mock_ticker

        analyzer = FinancialAnalyzer()
        result = analyzer.fetch_stock_data("AAPL")

        assert result == mock_data
        assert analyzer.data == mock_data
        mock_yf.Ticker.assert_called_once_with("AAPL")
        mock_ticker.history.assert_called_once_with(period="1y")

    def test_fetch_stock_data_no_yfinance(self) -> None:
        """Test behavior when yfinance is not available."""
        with patch("ai_financial_tool.main.yf", None):
            analyzer = FinancialAnalyzer()
            result = analyzer.fetch_stock_data("AAPL")
            assert result is None

    def test_calculate_returns_no_data(self) -> None:
        """Test calculate_returns with no data."""
        analyzer = FinancialAnalyzer()
        result = analyzer.calculate_returns()
        assert result is None

    def test_analyze_volatility_no_data(self) -> None:
        """Test analyze_volatility with no data."""
        analyzer = FinancialAnalyzer()
        result = analyzer.analyze_volatility()
        assert result is None

    def test_generate_summary_no_data(self) -> None:
        """Test generate_summary with no data."""
        analyzer = FinancialAnalyzer()
        result = analyzer.generate_summary("AAPL")
        assert "error" in result


def test_setup_logging() -> None:
    """Test that setup_logging doesn't raise an exception."""
    # This test ensures the function can be called without errors
    setup_logging("INFO")
    setup_logging("DEBUG")
    setup_logging("WARNING")


class TestSetupLoggingParameterized:
    """Parametrized tests for the setup_logging function."""

    @pytest.mark.parametrize(
        "level",
        ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    )
    def test_setup_logging_levels(self, level: str) -> None:
        """Test setup_logging with various log levels."""
        # Should not raise any exceptions
        setup_logging(level)
