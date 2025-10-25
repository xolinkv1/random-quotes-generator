# Quick Start Guide

Get up and running with Random Quotes Generator in 5 minutes! ⚡

## 🚀 Installation (30 seconds)

```bash
# Clone the repository
git clone https://github.com/kiaraelix/random-quotes-generator.git
cd random-quotes-generator

# Install
pip install -e .
```

## 💡 First Quote (10 seconds)

```bash
# Get a random quote
python -m quotes_generator
```

Output:
```
"The only way to do great work is to love what you do."
  — Steve Jobs
  [motivation]
```

## 🎯 Common Commands

```bash
# Get a motivational quote
python -m quotes_generator --category motivation

# Get 3 random quotes
python -m quotes_generator --count 3

# Search by author
python -m quotes_generator --author "Einstein"

# View statistics
python -m quotes_generator --stats

# See all options
python -m quotes_generator --help
```

## 🐍 Python Usage

```python
from quotes_generator import QuoteGenerator

# Initialize
generator = QuoteGenerator()

# Get a quote
quote = generator.get_random_quote()
print(f'"{quote["text"]}" - {quote["author"]}')

# Filter by category
motivational = generator.get_random_quote(category="motivation")

# Get multiple quotes
quotes = generator.get_multiple_quotes(5)
```

## 📚 Next Steps

- Read the full [README](README.md)
- Check out [examples](docs/EXAMPLES.md)
- View [API documentation](docs/API.md)
- See [installation guide](docs/INSTALLATION.md)

## 🆘 Need Help?

- [Open an issue](https://github.com/kiaraelix/random-quotes-generator/issues)
- Check [troubleshooting](docs/INSTALLATION.md#troubleshooting)
- Read [contributing guide](docs/CONTRIBUTING.md)

---

**That's it! You're ready to get inspired! 🎯**
