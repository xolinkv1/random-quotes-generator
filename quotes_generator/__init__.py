"""
Random Quotes Generator
A professional Python package for generating random inspirational quotes.

This package provides a simple yet powerful interface for retrieving
inspirational quotes from a curated collection. It supports filtering
by category and author, searching, and exporting quotes.

Example:
    >>> from quotes_generator import QuoteGenerator
    >>> generator = QuoteGenerator()
    >>> quote = generator.get_random_quote()
    >>> print(quote["text"])
"""

__version__ = "1.0.0"
__author__ = "Kiara Sinha"
__email__ = "kiara@example.com"
__license__ = "MIT"
__url__ = "https://github.com/kiaraelix/random-quotes-generator"

from .generator import QuoteGenerator

__all__ = ["QuoteGenerator", "__version__"]
