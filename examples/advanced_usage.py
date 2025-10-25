"""
Advanced usage examples for the Random Quotes Generator.
"""

from quotes_generator import QuoteGenerator
import json


def main():
    """Demonstrate advanced features of the QuoteGenerator."""
    
    generator = QuoteGenerator()
    
    # Get collection statistics
    print("📊 Collection Statistics")
    print("=" * 60)
    stats = generator.get_statistics()
    print(f"Total Quotes: {stats['total_quotes']}")
    print(f"Total Categories: {stats['total_categories']}")
    print(f"Total Authors: {stats['total_authors']}")
    print(f"Average Quote Length: {stats['average_quote_length']:.0f} characters\n")
    
    print("Top 5 Categories:")
    for category, count in sorted(stats['categories'].items(), 
                                   key=lambda x: x[1], reverse=True)[:5]:
        print(f"  • {category}: {count} quotes")
    print()
    
    print("Top Authors:")
    for author, count in stats['top_authors'].items():
        print(f"  • {author}: {count} quotes")
    print("\n")
    
    # Search functionality
    print("🔍 Search Results for 'success'")
    print("=" * 60)
    results = generator.search_quotes("success")
    print(f"Found {len(results)} quotes containing 'success':\n")
    for quote in results[:3]:  # Show first 3
        print(f'"{quote["text"]}"')
        print(f"— {quote['author']}\n")
    
    # Get all authors
    print("👥 All Authors in Collection")
    print("=" * 60)
    authors = sorted(generator.get_all_authors())
    for author in authors[:10]:  # Show first 10
        count = len(generator.get_quotes_by_author(author))
        print(f"  • {author} ({count} quote{'s' if count > 1 else ''})")
    print(f"\n... and {len(authors) - 10} more authors\n")
    
    # Export quotes
    print("💾 Exporting Quotes")
    print("=" * 60)
    output_file = "exported_quotes.json"
    generator.export_quotes(output_file, category="motivation")
    print(f"✓ Exported motivational quotes to {output_file}")
    
    # Read and display exported file info
    with open(output_file, 'r') as f:
        exported = json.load(f)
        print(f"✓ Exported {len(exported['quotes'])} quotes\n")
    
    # Category-specific analysis
    print("📈 Category Analysis")
    print("=" * 60)
    for category in sorted(generator.get_categories())[:5]:
        category_quotes = [q for q in generator.quotes 
                          if q['category'] == category]
        avg_length = sum(len(q['text']) for q in category_quotes) / len(category_quotes)
        print(f"{category.capitalize()}: {len(category_quotes)} quotes, "
              f"avg length: {avg_length:.0f} chars")


if __name__ == "__main__":
    main()
