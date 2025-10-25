"""
Unit tests for the formatter module.
"""

import unittest
from quotes_generator.formatter import format_quote, format_statistics, print_header


class TestFormatter(unittest.TestCase):
    """Test cases for formatter functions."""

    def setUp(self):
        """Set up test fixtures."""
        self.sample_quote = {
            "text": "Test quote",
            "author": "Test Author",
            "category": "test"
        }
        
        self.sample_stats = {
            "total_quotes": 50,
            "total_categories": 10,
            "total_authors": 25,
            "average_quote_length": 100.5,
            "categories": {
                "motivation": 15,
                "wisdom": 10,
                "success": 8
            },
            "top_authors": {
                "Steve Jobs": 3,
                "Albert Einstein": 2
            }
        }

    def test_format_quote_with_color(self):
        """Test formatting quote with colors."""
        result = format_quote(self.sample_quote, no_color=False)
        self.assertIn("Test quote", result)
        self.assertIn("Test Author", result)
        self.assertIn("test", result)
        self.assertIn("\033[", result)  # Check for ANSI codes

    def test_format_quote_without_color(self):
        """Test formatting quote without colors."""
        result = format_quote(self.sample_quote, no_color=True)
        self.assertIn("Test quote", result)
        self.assertIn("Test Author", result)
        self.assertIn("test", result)
        self.assertNotIn("\033[", result)  # No ANSI codes

    def test_format_statistics_with_color(self):
        """Test formatting statistics with colors."""
        result = format_statistics(self.sample_stats, no_color=False)
        self.assertIn("Total Quotes: 50", result)
        self.assertIn("Total Categories: 10", result)
        self.assertIn("Total Authors: 25", result)
        self.assertIn("motivation: 15", result)
        self.assertIn("Steve Jobs: 3", result)

    def test_format_statistics_without_color(self):
        """Test formatting statistics without colors."""
        result = format_statistics(self.sample_stats, no_color=True)
        self.assertIn("Total Quotes: 50", result)
        self.assertNotIn("\033[", result)  # No ANSI codes


if __name__ == "__main__":
    unittest.main()
