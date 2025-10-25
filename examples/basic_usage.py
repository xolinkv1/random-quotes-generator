"""
Basic usage examples for the Random Quotes Generator.
"""

from quotes_generator import QuoteGenerator


def main():
    """Demonstrate basic usage of the QuoteGenerator."""
    
    # Initialize the generator
    print("Initializing Quote Generator...\n")
    generator = QuoteGenerator()
    
    # Get a random quote
    print("1. Random Quote:")
    print("-" * 50)
    quote = generator.get_random_quote()
    print(f'"{quote["text"]}"')
    print(f"— {quote['author']}")
    print(f"[{quote['category']}]\n")
    
    # Get a quote by category
    print("2. Motivational Quote:")
    print("-" * 50)
    motivational = generator.get_random_quote(category="motivation")
    if motivational:
        print(f'"{motivational["text"]}"')
        print(f"— {motivational['author']}\n")
    
    # List all categories
    print("3. Available Categories:")
    print("-" * 50)
    categories = generator.get_categories()
    for category in sorted(categories):
        print(f"  • {category}")
    print()
    
    # Get quotes by author
    print("4. Quotes by Steve Jobs:")
    print("-" * 50)
    jobs_quotes = generator.get_quotes_by_author("Steve Jobs")
    for quote in jobs_quotes:
        print(f'  • "{quote["text"]}"')
    print()
    
    # Get multiple random quotes
    print("5. Three Random Quotes:")
    print("-" * 50)
    multiple = generator.get_multiple_quotes(3)
    for i, quote in enumerate(multiple, 1):
        print(f'{i}. "{quote["text"]}" — {quote["author"]}')
    print()


if __name__ == "__main__":
    main()
