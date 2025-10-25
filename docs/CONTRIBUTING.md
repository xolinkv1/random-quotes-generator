# Contributing to Random Quotes Generator

Thank you for your interest in contributing to the Random Quotes Generator! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive feedback
- Respect differing viewpoints and experiences

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment (OS, Python version)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please create an issue with:
- A clear description of the enhancement
- Why this enhancement would be useful
- Possible implementation approach

### Adding New Quotes

To add new quotes to the collection:

1. Edit `quotes_generator/data/quotes.json`
2. Follow the existing format:
```json
{
  "text": "Your quote here",
  "author": "Author Name",
  "category": "appropriate_category"
}
```
3. Ensure the quote is:
   - Inspirational or thought-provoking
   - Properly attributed
   - Categorized appropriately
   - Free from offensive content

### Pull Request Process

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`python -m pytest`)
5. Run linting (`flake8 quotes_generator tests`)
6. Format code (`black quotes_generator tests`)
7. Commit your changes (`git commit -m 'Add amazing feature'`)
8. Push to the branch (`git push origin feature/amazing-feature`)
9. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/random-quotes-generator.git
cd random-quotes-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install in development mode
pip install -e .
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=quotes_generator --cov-report=html

# Run specific test file
python -m pytest tests/test_generator.py
```

### Code Style

- Follow PEP 8 guidelines
- Use Black for code formatting
- Write docstrings for all functions and classes
- Keep functions focused and concise
- Add type hints where appropriate

### Commit Messages

- Use clear, descriptive commit messages
- Start with a verb in present tense (Add, Fix, Update, etc.)
- Keep the first line under 50 characters
- Add detailed description if needed

Examples:
```
Add search functionality to quote generator
Fix category filtering bug
Update documentation with new examples
```

## Questions?

Feel free to open an issue for any questions or concerns!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
