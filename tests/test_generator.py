"""
Unit tests for the QuoteGenerator class.
"""

import unittest
import json
import tempfile
from pathlib import Path
from quotes_generator.generator import QuoteGenerator


class TestQuoteGenerator(unittest.TestCase):
    """Test cases for QuoteGenerator."""

    def setUp(self):
        """Set up test fixtures."""
        self.test_quotes = {
            "quotes": [
                {
                    "text": "Test quote 1",
                    "author": "Author 1",
                    "category": "test"
                },
                {
                    "text": "Test quote 2",
                    "author": "Author 2",
                    "category": "motivation"
                },
                {
                    "text": "Test quote 3",
                    "author": "Author 1",
                    "category": "test"
                },
                {
                    "text": "Test quote 4",
                    "author": "Author 3",
                    "category": "wisdom"
                }
            ]
        }
        
        # Create temporary quotes file
        self.temp_file = tempfile.NamedTemporaryFile(
            mode='w', delete=False, suffix='.json'
        )
        json.dump(self.test_quotes, self.temp_file)
        self.temp_file.close()
        
        self.generator = QuoteGenerator(self.temp_file.name)

    def tearDown(self):
        """Clean up test fixtures."""
        Path(self.temp_file.name).unlink()

    def test_load_quotes(self):
        """Test that quotes are loaded correctly."""
        self.assertEqual(len(self.generator.quotes), 4)

    def test_get_random_quote(self):
        """Test getting a random quote."""
        quote = self.generator.get_random_quote()
        self.assertIsNotNone(quote)
        self.assertIn("text", quote)
        self.assertIn("author", quote)
        self.assertIn("category", quote)

    def test_get_random_quote_by_category(self):
        """Test filtering quotes by category."""
        quote = self.generator.get_random_quote(category="test")
        self.assertIsNotNone(quote)
        self.assertEqual(quote["category"], "test")

    def test_get_random_quote_invalid_category(self):
        """Test that invalid category returns None."""
        quote = self.generator.get_random_quote(category="nonexistent")
        self.assertIsNone(quote)

    def test_get_categories(self):
        """Test getting all categories."""
        categories = self.generator.get_categories()
        self.assertEqual(len(categories), 3)
        self.assertIn("test", categories)
        self.assertIn("motivation", categories)
        self.assertIn("wisdom", categories)

    def test_get_quotes_by_author(self):
        """Test filtering quotes by author."""
        quotes = self.generator.get_quotes_by_author("Author 1")
        self.assertEqual(len(quotes), 2)
        
    def test_get_quotes_by_author_case_insensitive(self):
        """Test that author search is case-insensitive."""
        quotes = self.generator.get_quotes_by_author("author 1")
        self.assertEqual(len(quotes), 2)

    def test_get_all_authors(self):
        """Test getting all unique authors."""
        authors = self.generator.get_all_authors()
        self.assertEqual(len(authors), 3)
        self.assertIn("Author 1", authors)
        self.assertIn("Author 2", authors)
        self.assertIn("Author 3", authors)

    def test_get_multiple_quotes(self):
        """Test getting multiple quotes."""
        quotes = self.generator.get_multiple_quotes(2)
        self.assertEqual(len(quotes), 2)
        
    def test_get_multiple_quotes_with_category(self):
        """Test getting multiple quotes with category filter."""
        quotes = self.generator.get_multiple_quotes(2, category="test")
        self.assertEqual(len(quotes), 2)
        for quote in quotes:
            self.assertEqual(quote["category"], "test")

    def test_get_statistics(self):
        """Test getting collection statistics."""
        stats = self.generator.get_statistics()
        self.assertEqual(stats["total_quotes"], 4)
        self.assertEqual(stats["total_categories"], 3)
        self.assertEqual(stats["total_authors"], 3)
        self.assertIn("categories", stats)
        self.assertIn("top_authors", stats)

    def test_search_quotes(self):
        """Test searching quotes by keyword."""
        results = self.generator.search_quotes("Test")
        self.assertEqual(len(results), 4)
        
    def test_search_quotes_no_results(self):
        """Test searching with no matching results."""
        results = self.generator.search_quotes("nonexistent")
        self.assertEqual(len(results), 0)

    def test_export_quotes(self):
        """Test exporting quotes to file."""
        output_file = tempfile.NamedTemporaryFile(
            mode='w', delete=False, suffix='.json'
        )
        output_file.close()
        
        try:
            self.generator.export_quotes(output_file.name)
            
            with open(output_file.name, 'r') as f:
                data = json.load(f)
                self.assertEqual(len(data["quotes"]), 4)
        finally:
            Path(output_file.name).unlink()

    def test_validate_quotes_missing_fields(self):
        """Test that validation catches missing required fields."""
        invalid_quotes = {
            "quotes": [
                {
                    "text": "Invalid quote",
                    "author": "Author"
                    # Missing category
                }
            ]
        }
        
        temp_file = tempfile.NamedTemporaryFile(
            mode='w', delete=False, suffix='.json'
        )
        json.dump(invalid_quotes, temp_file)
        temp_file.close()
        
        try:
            with self.assertRaises(ValueError):
                QuoteGenerator(temp_file.name)
        finally:
            Path(temp_file.name).unlink()

    def test_file_not_found(self):
        """Test that FileNotFoundError is raised for missing file."""
        with self.assertRaises(FileNotFoundError):
            QuoteGenerator("nonexistent_file.json")


if __name__ == "__main__":
    unittest.main()
