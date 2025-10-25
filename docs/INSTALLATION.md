# Installation Guide

Complete installation instructions for the Random Quotes Generator.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation Methods](#installation-methods)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

### System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python**: Version 3.7 or higher
- **pip**: Python package installer (usually included with Python)
- **Git**: For cloning the repository (optional)

### Check Your Python Version

```bash
python --version
# or
python3 --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

---

## Installation Methods

### Method 1: Clone from GitHub (Recommended)

This method is best for development and getting the latest features.

```bash
# 1. Clone the repository
git clone https://github.com/kiaraelix/random-quotes-generator.git

# 2. Navigate to the project directory
cd random-quotes-generator

# 3. Create a virtual environment (recommended)
python -m venv venv

# 4. Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# 5. Install the package in development mode
pip install -e .
```

### Method 2: Direct Installation from GitHub

Install directly without cloning:

```bash
pip install git+https://github.com/kiaraelix/random-quotes-generator.git
```

### Method 3: Download ZIP

1. Go to https://github.com/kiaraelix/random-quotes-generator
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file
4. Open terminal in the extracted folder
5. Run: `pip install -e .`

---

## Virtual Environment Setup

### Why Use a Virtual Environment?

- Isolates project dependencies
- Prevents conflicts with other projects
- Makes dependency management easier
- Recommended best practice

### Creating a Virtual Environment

#### Windows

```bash
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate

# Deactivate (when done)
deactivate
```

#### macOS/Linux

```bash
# Create virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate

# Deactivate (when done)
deactivate
```

---

## Development Installation

For contributing or development:

```bash
# 1. Clone and navigate
git clone https://github.com/kiaraelix/random-quotes-generator.git
cd random-quotes-generator

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 4. Install in editable mode
pip install -e .

# 5. Verify installation
python -m pytest
```

---

## Verification

### Verify Installation

```bash
# Check if the package is installed
pip list | grep random-quotes-generator

# Test the CLI
python -m quotes_generator

# Test the Python API
python -c "from quotes_generator import QuoteGenerator; print('Success!')"
```

### Run Tests

```bash
# Run all tests
python -m pytest

# Run with verbose output
python -m pytest -v

# Check test coverage
python -m pytest --cov=quotes_generator
```

### Check Version

```python
from quotes_generator import __version__
print(__version__)
```

---

## Troubleshooting

### Common Issues

#### Issue: "python: command not found"

**Solution**: Python is not installed or not in PATH.

```bash
# Try python3 instead
python3 --version

# Or install Python from python.org
```

#### Issue: "pip: command not found"

**Solution**: pip is not installed.

```bash
# Install pip
python -m ensurepip --upgrade

# Or use python3
python3 -m ensurepip --upgrade
```

#### Issue: "Permission denied"

**Solution**: Use a virtual environment or install with --user flag.

```bash
# Option 1: Use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install -e .

# Option 2: Install for current user only
pip install --user -e .
```

#### Issue: "Module not found"

**Solution**: Ensure you're in the correct directory and virtual environment is activated.

```bash
# Check current directory
pwd  # or cd on Windows

# Activate virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Reinstall
pip install -e .
```

#### Issue: Tests failing

**Solution**: Install development dependencies.

```bash
pip install -r requirements-dev.txt
python -m pytest
```

#### Issue: Import errors

**Solution**: Reinstall the package.

```bash
pip uninstall random-quotes-generator
pip install -e .
```

---

## Updating

### Update to Latest Version

```bash
# Navigate to project directory
cd random-quotes-generator

# Pull latest changes
git pull origin main

# Reinstall
pip install -e .
```

---

## Uninstallation

### Remove the Package

```bash
# Uninstall the package
pip uninstall random-quotes-generator

# Remove virtual environment (optional)
rm -rf venv  # or rmdir /s venv on Windows

# Remove project directory (optional)
cd ..
rm -rf random-quotes-generator
```

---

## Platform-Specific Notes

### Windows

- Use `python` instead of `python3`
- Use `venv\Scripts\activate` to activate virtual environment
- Use backslashes `\` in paths
- May need to run PowerShell as Administrator

### macOS

- Use `python3` and `pip3`
- May need to install Xcode Command Line Tools
- Use `source venv/bin/activate`

### Linux

- Use `python3` and `pip3`
- May need to install `python3-venv` package
- Use `source venv/bin/activate`

```bash
# Ubuntu/Debian
sudo apt-get install python3-venv

# Fedora
sudo dnf install python3-virtualenv

# Arch
sudo pacman -S python-virtualenv
```

---

## Docker Installation (Optional)

For containerized deployment:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -e .

CMD ["python", "-m", "quotes_generator"]
```

Build and run:

```bash
docker build -t quotes-generator .
docker run quotes-generator
```

---

## Next Steps

After installation:

1. ✅ Read the [README](../README.md)
2. ✅ Try the [examples](EXAMPLES.md)
3. ✅ Check the [API documentation](API.md)
4. ✅ Run `python -m quotes_generator --help`

---

## Support

If you encounter issues:

1. Check this troubleshooting guide
2. Search [existing issues](https://github.com/kiaraelix/random-quotes-generator/issues)
3. Create a [new issue](https://github.com/kiaraelix/random-quotes-generator/issues/new)

---

*Happy quoting! 🎯*
