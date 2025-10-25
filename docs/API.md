# API Documentation

Complete API reference for the Random Quotes Generator package.

## Table of Contents

- [QuoteGenerator Class](#quotegenerator-class)
- [Methods](#methods)
- [Data Structures](#data-structures)
- [Examples](#examples)

## QuoteGenerator Class

The main class for interacting with the quote collection.

### Constructor

```python
QuoteGenerator(quotes_file: Optional[str] = None)
```

**Parameters:**
- `quotes_file` (str, optional): Path to a custom quotes JSON file. If None, uses the default collection.

**Raises:**
- `FileNotFoundError`: If the specified quotes file doesn't exist
- `ValueError`: If the quotes file contains invalid JSON or missing required fields

**Example:**
```python
# Use default quotes
generator = QuoteGenerator()

# Use custom quotes file
generator = QuoteGenerator("path/to/custom_quotes.json")
```

## Methods

### get_random_quote

```python
get_random_quote(category: Optional[str] = None) -> Optional[Dict[str, str]]
```

Get a random quote, optionally filtered by category.

**Parameters:**
- `category` (str, optional): Filter quotes by this category

**Returns:**
- `Dict[str, str]`: Quote dictionary with keys: `text`, `author`, `category`
- `None`: If no quotes match the specified category

**Example:**
```python
# Random quote from any category
quote = generator.get_random_quote()

# Random motivational quote
quote = generator.get_random_quote(category="motivation")
```

---

### get_multiple_quotes

```python
get_multiple_quotes(count: int, category: Optional[str] = None) -> List[Dict[str, str]]
```

Get multiple random quotes.

**Parameters:**
- `count` (int): Number of quotes to retrieve
- `category` (str, optional): Filter quotes by category

**Returns:**
- `List[Dict[str, str]]`: List of quote dictionaries

**Example:**
```python
# Get 5 random quotes
quotes = generator.get_multiple_quotes(5)

# Get 3 wisdom quotes
quotes = generator.get_multiple_quotes(3, category="wisdom")
```

---

### get_quotes_by_author

```python
get_quotes_by_author(author: str) -> List[Dict[str, str]]
```

Get all quotes by a specific author (case-insensitive partial match).

**Parameters:**
- `author` (str): Author name to search for

**Returns:**
- `List[Dict[str, str]]`: List of matching quotes

**Example:**
```python
# Get all Steve Jobs quotes
jobs_quotes = generator.get_quotes_by_author("Steve Jobs")

# Partial match works too
jobs_quotes = generator.get_quotes_by_author("Jobs")
```

---

### search_quotes

```python
search_quotes(keyword: str) -> List[Dict[str, str]]
```

Search for quotes containing a specific keyword (case-insensitive).

**Parameters:**
- `keyword` (str): Keyword to search for in quote text

**Returns:**
- `List[Dict[str, str]]`: List of matching quotes

**Example:**
```python
# Find quotes about success
results = generator.search_quotes("success")

# Find quotes about dreams
results = generator.search_quotes("dream")
```

---

### get_categories

```python
get_categories() -> Set[str]
```

Get all available quote categories.

**Returns:**
- `Set[str]`: Set of category names

**Example:**
```python
categories = generator.get_categories()
print(f"Available: {', '.join(sorted(categories))}")
```

---

### get_all_authors

```python
get_all_authors() -> Set[str]
```

Get all unique authors in the collection.

**Returns:**
- `Set[str]`: Set of author names

**Example:**
```python
authors = generator.get_all_authors()
print(f"Collection includes {len(authors)} authors")
```

---

### get_statistics

```python
get_statistics() -> Dict[str, any]
```

Get statistical information about the quote collection.

**Returns:**
- `Dict`: Dictionary containing:
  - `total_quotes` (int): Total number of quotes
  - `total_categories` (int): Number of unique categories
  - `total_authors` (int): Number of unique authors
  - `categories` (Dict[str, int]): Quote count per category
  - `top_authors` (Dict[str, int]): Top 5 authors by quote count
  - `average_quote_length` (float): Average character length of quotes

**Example:**
```python
stats = generator.get_statistics()
print(f"Total quotes: {stats['total_quotes']}")
print(f"Most popular category: {max(stats['categories'], key=stats['categories'].get)}")
```

---

### export_quotes

```python
export_quotes(output_file: str, category: Optional[str] = None) -> None
```

Export quotes to a JSON file.

**Parameters:**
- `output_file` (str): Path to output file
- `category` (str, optional): Export only quotes from this category

**Raises:**
- `IOError`: If unable to write to the output file

**Example:**
```python
# Export all quotes
generator.export_quotes("all_quotes.json")

# Export only motivational quotes
generator.export_quotes("motivation.json", category="motivation")
```

## Data Structures

### Quote Dictionary

Each quote is represented as a dictionary with the following structure:

```python
{
    "text": str,      # The quote text
    "author": str,    # The author's name
    "category": str   # The quote category
}
```

**Example:**
```python
{
    "text": "The only way to do great work is to love what you do.",
    "author": "Steve Jobs",
    "category": "motivation"
}
```

### Statistics Dictionary

The statistics dictionary returned by `get_statistics()`:

```python
{
    "total_quotes": int,
    "total_categories": int,
    "total_authors": int,
    "categories": Dict[str, int],
    "top_authors": Dict[str, int],
    "average_quote_length": float
}
```

## Examples

### Basic Usage

```python
from quotes_generator import QuoteGenerator

# Initialize
generator = QuoteGenerator()

# Get a random quote
quote = generator.get_random_quote()
print(f'"{quote["text"]}" - {quote["author"]}')
```

### Advanced Usage

```python
# Get multiple quotes from a specific category
wisdom_quotes = generator.get_multiple_quotes(5, category="wisdom")

# Search and filter
success_quotes = generator.search_quotes("success")
einstein_quotes = generator.get_quotes_by_author("Einstein")

# Analytics
stats = generator.get_statistics()
categories = generator.get_categories()
authors = generator.get_all_authors()

# Export
generator.export_quotes("my_collection.json")
```

### Integration Example

```python
def daily_motivation_bot():
    """Send a daily motivational quote."""
    generator = QuoteGenerator()
    quote = generator.get_random_quote(category="motivation")
    
    message = f"""
    🌟 Daily Motivation 🌟
    
    "{quote['text']}"
    
    — {quote['author']}
    """
    
    return message
```

## Error Handling

```python
from quotes_generator import QuoteGenerator

try:
    generator = QuoteGenerator("custom_quotes.json")
    quote = generator.get_random_quote()
except FileNotFoundError:
    print("Quotes file not found!")
except ValueError as e:
    print(f"Invalid quotes file: {e}")
```

## Thread Safety

The `QuoteGenerator` class is thread-safe for read operations. Multiple threads can safely call methods like `get_random_quote()` simultaneously.

## Performance

- Quote loading: O(n) where n is the number of quotes
- Random quote retrieval: O(1) for unfiltered, O(n) for filtered
- Search operations: O(n)
- Category/Author filtering: O(n)

For large collections (1000+ quotes), consider implementing caching or indexing strategies.
