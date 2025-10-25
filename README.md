<div align="center">

# ðŸŽ¯ Random Quotes Generator

### *Inspire, Motivate, Transform*

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://github.com/kiaraelix/random-quotes-generator)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/kiaraelix/random-quotes-generator/pulls)

A professional, feature-rich Python package for generating random inspirational quotes. Perfect for CLI tools, web applications, chatbots, daily motivation scripts, or integrating wisdom into your projects.

[Features](#-features) â€¢ [Installation](#-installation) â€¢ [Usage](#-usage) â€¢ [API](#-api-reference) â€¢ [Contributing](#-contributing)

</div>

---

## âœ¨ Features

<table>
<tr>
<td width="50%">

### Core Functionality
- ðŸŽ² **Random Quote Generation** - Instant access to inspiring quotes
- ðŸ·ï¸ **Smart Filtering** - Filter by 20+ categories
- ðŸ‘¤ **Author Search** - Find quotes by your favorite thinkers
- ï¿½ ***Keyword Search** - Search quotes by content
- ðŸ“Š **Statistics & Analytics** - Insights into your collection
- ðŸ’¾ **Export Capability** - Save quotes to JSON files

</td>
<td width="50%">

### Developer Experience
- ðŸ’» **Rich CLI Interface** - Beautiful command-line tool
- ðŸŽ¨ **Colored Output** - Terminal formatting with ANSI colors
- ðŸ“¦ **Zero Dependencies** - Pure Python implementation
- ðŸ§ª **100% Test Coverage** - Comprehensive unit tests
- ðŸ”§ **Highly Extensible** - Easy to customize and extend
- ðŸ“š **Well Documented** - Clear API and examples

</td>
</tr>
</table>

## ðŸš€ Installation

### Quick Install

```bash
# Clone the repository
git clone https://github.com/kiaraelix/random-quotes-generator.git
cd random-quotes-generator

# Create and activate virtual environment (recommended)
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# Install the package
pip install -e .
```

### Alternative: Direct Installation

```bash
# Install from source
pip install git+https://github.com/kiaraelix/random-quotes-generator.git
```

## ðŸ’¡ Usage

### Command Line Interface

The package provides a powerful CLI with multiple commands:

```bash
# Get a random quote
quotes

# Filter by category
quotes --category motivation

# Search by author
quotes --author "Steve Jobs"

# Get multiple quotes
quotes --count 5

# Search for keywords
quotes --search "success"

# View statistics
quotes --stats

# List all categories
quotes --list-categories

# List all authors
quotes --list-authors

# Export quotes to file
quotes --export my_quotes.json --category wisdom

# Disable colored output
quotes --no-color
```

### Quick Examples

```bash
# Morning motivation
quotes --category motivation

# Get 3 wisdom quotes
quotes --category wisdom --count 3

# Find all Einstein quotes
quotes --author "Einstein"

# Export all motivational quotes
quotes --export motivation.json --category motivation
```

## ðŸ“š API Reference

### Python Integration

Integrate quotes into your Python applications:

```python
from quotes_generator import QuoteGenerator

# Initialize the generator
generator = QuoteGenerator()

# Get a random quote
quote = generator.get_random_quote()
print(f'"{quote["text"]}" - {quote["author"]}')
# Output: "The only way to do great work is to love what you do." - Steve Jobs
```

### Core Methods

#### `get_random_quote(category=None)`
Get a random quote, optionally filtered by category.

```python
# Random quote from any category
quote = generator.get_random_quote()

# Random motivational quote
quote = generator.get_random_quote(category="motivation")
```

#### `get_multiple_quotes(count, category=None)`
Get multiple random quotes at once.

```python
# Get 5 random quotes
quotes = generator.get_multiple_quotes(5)

# Get 3 wisdom quotes
quotes = generator.get_multiple_quotes(3, category="wisdom")
```

#### `get_quotes_by_author(author)`
Find all quotes by a specific author.

```python
# Get all Steve Jobs quotes
jobs_quotes = generator.get_quotes_by_author("Steve Jobs")

for quote in jobs_quotes:
    print(f"â€¢ {quote['text']}")
```

#### `search_quotes(keyword)`
Search for quotes containing a keyword.

```python
# Find quotes about success
results = generator.search_quotes("success")
print(f"Found {len(results)} quotes about success")
```

#### `get_statistics()`
Get detailed statistics about the quote collection.

```python
stats = generator.get_statistics()
print(f"Total quotes: {stats['total_quotes']}")
print(f"Total authors: {stats['total_authors']}")
print(f"Categories: {stats['categories']}")
```

#### `get_categories()`
Get all available categories.

```python
categories = generator.get_categories()
print(f"Available: {', '.join(sorted(categories))}")
```

#### `get_all_authors()`
Get all unique authors in the collection.

```python
authors = generator.get_all_authors()
print(f"Collection includes {len(authors)} authors")
```

#### `export_quotes(output_file, category=None)`
Export quotes to a JSON file.

```python
# Export all quotes
generator.export_quotes("all_quotes.json")

# Export only motivational quotes
generator.export_quotes("motivation.json", category="motivation")
```

### Advanced Usage Examples

```python
# Daily quote script
def get_daily_quote():
    generator = QuoteGenerator()
    quote = generator.get_random_quote()
    return f"ðŸ’­ {quote['text']}\n   â€” {quote['author']}"

# Category-based quote selector
def get_quote_for_mood(mood):
    mood_map = {
        "motivated": "motivation",
        "thoughtful": "wisdom",
        "ambitious": "success"
    }
    category = mood_map.get(mood, None)
    generator = QuoteGenerator()
    return generator.get_random_quote(category=category)

# Quote analytics
def analyze_collection():
    generator = QuoteGenerator()
    stats = generator.get_statistics()
    
    print(f"ðŸ“Š Collection Analysis")
    print(f"Total Quotes: {stats['total_quotes']}")
    print(f"Most Popular Category: {max(stats['categories'], key=stats['categories'].get)}")
    print(f"Average Quote Length: {stats['average_quote_length']:.0f} characters")
```

## ðŸ“ Project Structure

```
random-quotes-generator/
â”œâ”€â”€ quotes_generator/           # Main package
â”‚   â”œâ”€â”€ __init__.py            # Package initialization
â”‚   â”œâ”€â”€ __main__.py            # CLI entry point
â”‚   â”œâ”€â”€ generator.py           # Core quote generator
â”‚   â”œâ”€â”€ formatter.py           # Output formatting utilities
â”‚   â””â”€â”€ data/
â”‚       â””â”€â”€ quotes.json        # Quote database (50+ quotes)
â”œâ”€â”€ tests/                     # Test suite
â”‚   â”œâ”€â”€ __init__.py
â”‚   â”œâ”€â”€ test_generator.py     # Generator tests
â”‚   â””â”€â”€ test_formatter.py     # Formatter tests
â”œâ”€â”€ examples/                  # Usage examples
â”‚   â”œâ”€â”€ basic_usage.py
â”‚   â””â”€â”€ advanced_usage.py
â”œâ”€â”€ docs/                      # Documentation
â”‚   â””â”€â”€ CONTRIBUTING.md
â”œâ”€â”€ .gitignore                 # Git ignore rules
â”œâ”€â”€ LICENSE                    # MIT License
â”œâ”€â”€ README.md                  # This file
â”œâ”€â”€ requirements.txt           # Production dependencies
â”œâ”€â”€ requirements-dev.txt       # Development dependencies
â””â”€â”€ setup.py                   # Package configuration
```

## ðŸŽ¨ Customization

### Adding Your Own Quotes

You can easily extend the quote collection by editing `quotes_generator/data/quotes.json`:

```json
{
  "quotes": [
    {
      "text": "Your inspiring quote here",
      "author": "Author Name",
      "category": "motivation"
    },
    {
      "text": "Another brilliant quote",
      "author": "Famous Person",
      "category": "wisdom"
    }
  ]
}
```

### Available Categories

The collection includes quotes from these categories:

`motivation` â€¢ `wisdom` â€¢ `success` â€¢ `innovation` â€¢ `life` â€¢ `action` â€¢ `perseverance` â€¢ `courage` â€¢ `ambition` â€¢ `work` â€¢ `inspiration` â€¢ `empowerment` â€¢ `purpose` â€¢ `achievement` â€¢ `values` â€¢ `dreams` â€¢ `excellence` â€¢ `potential` â€¢ `belief` â€¢ `mindset`

### Using Custom Quote Files

```python
from quotes_generator import QuoteGenerator

# Load quotes from a custom file
generator = QuoteGenerator(quotes_file="path/to/your/quotes.json")
quote = generator.get_random_quote()
```

## ðŸ§ª Development & Testing

### Running Tests

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run all tests
python -m pytest

# Run with verbose output
python -m pytest -v

# Run specific test file
python -m pytest tests/test_generator.py

# Run with coverage report
python -m pytest --cov=quotes_generator --cov-report=html
```

### Code Quality

```bash
# Format code with Black
black quotes_generator tests examples

# Lint with flake8
flake8 quotes_generator tests

# Type checking with mypy
mypy quotes_generator
```

### Project Statistics

```bash
# View collection statistics
python -m quotes_generator --stats

# Run example scripts
python examples/basic_usage.py
python examples/advanced_usage.py
```

## ðŸ¤ Contributing

We love contributions! Whether it's bug fixes, new features, or additional quotes, your help is appreciated.

### How to Contribute

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/YOUR_USERNAME/random-quotes-generator.git`
3. **Create** a feature branch: `git checkout -b feature/amazing-feature`
4. **Make** your changes and test them
5. **Commit** your changes: `git commit -m 'Add amazing feature'`
6. **Push** to the branch: `git push origin feature/amazing-feature`
7. **Open** a Pull Request

### Contribution Ideas

- ðŸ“ Add more inspirational quotes
- ðŸŒ Add multi-language support
- ðŸŽ¨ Improve CLI formatting
- ðŸ“š Enhance documentation
- ðŸ› Fix bugs or issues
- âœ¨ Suggest new features

Please read [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines, code of conduct, and development process.

### Contributors

Thanks to all contributors who help make this project better! ðŸ™

## ï¿½  Project Statistics

<div align="center">

| Metric | Value |
|--------|-------|
| ðŸ“ Total Quotes | 50+ |
| ðŸ·ï¸ Categories | 20+ |
| ðŸ‘¥ Authors | 40+ |
| ðŸ§ª Test Coverage | 100% |
| ï¿½ Python Support | 3.7+ |
| ðŸ“¦ Dependencies | 0 (core) |

</div>

## ðŸ—ºï¸ Roadmap

### Version 1.x (Current)
- [x] Core quote generation functionality
- [x] CLI interface with rich features
- [x] Category and author filtering
- [x] Search and export capabilities
- [x] Comprehensive test suite

### Version 2.0 (Planned)
- [ ] ðŸŒ Web API with FastAPI
- [ ] ðŸ’¾ Database backend (SQLite/PostgreSQL)
- [ ] ðŸŒ Multi-language support
- [ ] ðŸ“… Quote of the day feature
- [ ] ðŸ”— Social media sharing integration
- [ ] ðŸ“± Mobile-friendly web interface

### Version 3.0 (Future)
- [ ] ðŸ¤– AI-powered quote recommendations
- [ ] ðŸ‘¤ User accounts and favorites
- [ ] ðŸ“Š Advanced analytics dashboard
- [ ] ðŸŽ¨ Custom quote collections
- [ ] ðŸ”Œ REST API with authentication
- [ ] ðŸ“§ Email subscription service

## ðŸ™ Acknowledgments

- Inspired by the timeless wisdom of great thinkers and leaders
- Built with Python's elegance and simplicity
- Thanks to all the authors whose words inspire millions
- Grateful to the open-source community

## ðŸ‘©â€ðŸ’» Author

<div align="center">

**Kiara Sinha**

ML Engineer passionate about training predictive models, optimizing neural networks, and deploying AI solutions that transform industries and experiences.

[![GitHub](https://img.shields.io/badge/GitHub-kiaraelix-181717?style=for-the-badge&logo=github)](https://github.com/kiaraelix)

</div>

## ðŸ“ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License - Copyright (c) 2025 Kiara Sinha
```

## ðŸ’¬ Support

- ðŸ“« Found a bug? [Open an issue](https://github.com/kiaraelix/random-quotes-generator/issues)
- ðŸ’¡ Have a feature request? [Start a discussion](https://github.com/kiaraelix/random-quotes-generator/discussions)
- â­ Like this project? Give it a star!
- ðŸ”„ Want to contribute? Check out [CONTRIBUTING.md](docs/CONTRIBUTING.md)

---

<div align="center">

**Made with â¤ï¸ and Python**

â­ If you find this project useful, please consider giving it a star on GitHub! â­

[â¬† Back to Top](#-random-quotes-generator)

</div>

