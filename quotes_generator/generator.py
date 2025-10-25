"""
Core quote generator functionality.
"""

import json
import random
from pathlib import Path
from typing import Dict, List, Optional, Set
from collections import Counter


class QuoteGenerator:
    """
    Generate random quotes from a curated collection.
    
    This class provides methods to retrieve, filter, and analyze quotes
    from a JSON database. It supports filtering by category and author,
    as well as statistical analysis of the quote collection.
    
    Attributes:
        quotes_file (Path): Path to the quotes JSON file.
        quotes (List[Dict]): List of loaded quotes.
    """

    def __init__(self, quotes_file: Optional[str] = None):
        """
        Initialize the quote generator.

        Args:
            quotes_file: Path to custom quotes JSON file. If None, uses default.
            
        Raises:
            FileNotFoundError: If the quotes file doesn't exist.
            ValueError: If the quotes file contains invalid JSON.
        """
        if quotes_file is None:
            quotes_file = Path(__file__).parent / "data" / "quotes.json"
        
        self.quotes_file = Path(quotes_file)
        self.quotes = self._load_quotes()
        self._validate_quotes()

    def _load_quotes(self) -> List[Dict[str, str]]:
        """
        Load quotes from JSON file.
        
        Returns:
            List of quote dictionaries.
            
        Raises:
            FileNotFoundError: If quotes file not found.
            ValueError: If JSON is invalid.
        """
        try:
            with open(self.quotes_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("quotes", [])
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Quotes file not found: {self.quotes_file}"
            )
        except json.JSONDecodeError as e:
            raise ValueError(
                f"Invalid JSON format in quotes file: {self.quotes_file}\n{str(e)}"
            )

    def _validate_quotes(self) -> None:
        """
        Validate that all quotes have required fields.
        
        Raises:
            ValueError: If any quote is missing required fields.
        """
        required_fields = {"text", "author", "category"}
        for idx, quote in enumerate(self.quotes):
            missing = required_fields - set(quote.keys())
            if missing:
                raise ValueError(
                    f"Quote at index {idx} is missing required fields: {missing}"
                )

    def get_random_quote(self, category: Optional[str] = None) -> Optional[Dict[str, str]]:
        """
        Get a random quote, optionally filtered by category.

        Args:
            category: Filter quotes by this category. If None, returns any quote.

        Returns:
            Dictionary containing quote text, author, and category, or None if no match.
            
        Example:
            >>> generator = QuoteGenerator()
            >>> quote = generator.get_random_quote(category="motivation")
            >>> print(quote["text"])
        """
        if category:
            filtered_quotes = [
                q for q in self.quotes 
                if q.get("category", "").lower() == category.lower()
            ]
            if not filtered_quotes:
                return None
            return random.choice(filtered_quotes)
        
        return random.choice(self.quotes) if self.quotes else None

    def get_multiple_quotes(self, count: int, category: Optional[str] = None) -> List[Dict[str, str]]:
        """
        Get multiple random quotes.
        
        Args:
            count: Number of quotes to retrieve.
            category: Optional category filter.
            
        Returns:
            List of quote dictionaries.
        """
        quotes_pool = self.quotes
        if category:
            quotes_pool = [
                q for q in self.quotes 
                if q.get("category", "").lower() == category.lower()
            ]
        
        if not quotes_pool:
            return []
        
        # Use sample if count is less than pool size, otherwise use choices
        if count <= len(quotes_pool):
            return random.sample(quotes_pool, count)
        else:
            return random.choices(quotes_pool, k=count)

    def get_categories(self) -> Set[str]:
        """
        Get all available quote categories.

        Returns:
            Set of category names.
        """
        return {q.get("category", "uncategorized") for q in self.quotes}

    def get_quotes_by_author(self, author: str) -> List[Dict[str, str]]:
        """
        Get all quotes by a specific author.

        Args:
            author: Author name to filter by (case-insensitive partial match).

        Returns:
            List of quotes by the specified author.
            
        Example:
            >>> generator = QuoteGenerator()
            >>> jobs_quotes = generator.get_quotes_by_author("Steve Jobs")
        """
        return [
            q for q in self.quotes 
            if author.lower() in q.get("author", "").lower()
        ]

    def get_all_authors(self) -> Set[str]:
        """
        Get all unique authors in the collection.
        
        Returns:
            Set of author names.
        """
        return {q.get("author", "Unknown") for q in self.quotes}

    def get_statistics(self) -> Dict[str, any]:
        """
        Get statistical information about the quote collection.
        
        Returns:
            Dictionary containing various statistics.
        """
        categories = [q.get("category", "uncategorized") for q in self.quotes]
        authors = [q.get("author", "Unknown") for q in self.quotes]
        
        category_counts = Counter(categories)
        author_counts = Counter(authors)
        
        return {
            "total_quotes": len(self.quotes),
            "total_categories": len(set(categories)),
            "total_authors": len(set(authors)),
            "categories": dict(category_counts),
            "top_authors": dict(author_counts.most_common(5)),
            "average_quote_length": sum(len(q.get("text", "")) for q in self.quotes) / len(self.quotes) if self.quotes else 0,
        }

    def search_quotes(self, keyword: str) -> List[Dict[str, str]]:
        """
        Search for quotes containing a specific keyword.
        
        Args:
            keyword: Keyword to search for in quote text.
            
        Returns:
            List of matching quotes.
        """
        keyword_lower = keyword.lower()
        return [
            q for q in self.quotes 
            if keyword_lower in q.get("text", "").lower()
        ]

    def export_quotes(self, output_file: str, category: Optional[str] = None) -> None:
        """
        Export quotes to a JSON file.
        
        Args:
            output_file: Path to output file.
            category: Optional category filter.
        """
        quotes_to_export = self.quotes
        if category:
            quotes_to_export = [
                q for q in self.quotes 
                if q.get("category", "").lower() == category.lower()
            ]
        
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump({"quotes": quotes_to_export}, f, indent=2, ensure_ascii=False)
