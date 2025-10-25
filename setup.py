"""
Setup configuration for the Random Quotes Generator package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="random-quotes-generator",
    version="1.0.0",
    author="Kiara Sinha",
    author_email="kiara@example.com",
    description="A professional Python package for generating random inspirational quotes with CLI support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kiaraelix/random-quotes-generator",
    project_urls={
        "Bug Reports": "https://github.com/kiaraelix/random-quotes-generator/issues",
        "Source": "https://github.com/kiaraelix/random-quotes-generator",
        "Documentation": "https://github.com/kiaraelix/random-quotes-generator#readme",
    },
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    keywords="quotes, inspirational, motivation, cli, random, generator",
    python_requires=">=3.7",
    include_package_data=True,
    package_data={
        "quotes_generator": ["data/*.json"],
    },
    entry_points={
        "console_scripts": [
            "quotes=quotes_generator.__main__:main",
        ],
    },
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=0.990",
        ],
    },
)
