"""
Command-line interface for the Random Quotes Generator.
"""

import argparse
import sys
from .generator import QuoteGenerator
from .formatter import format_quote, format_statistics, print_header


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="🎯 Random Quotes Generator - Get inspired with wisdom from great minds",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                              Get a random quote
  %(prog)s --category motivation        Get a motivational quote
  %(prog)s --author "Steve Jobs"        Get quotes by Steve Jobs
  %(prog)s --count 3                    Get 3 random quotes
  %(prog)s --stats                      Show collection statistics
  %(prog)s --export output.json         Export all quotes to file
        """
    )
    
    parser.add_argument(
        "--category",
        type=str,
        help="Filter quotes by category (e.g., motivation, success, wisdom)",
    )
    
    parser.add_argument(
        "--author",
        type=str,
        help="Filter quotes by author name",
    )
    
    parser.add_argument(
        "--list-categories",
        action="store_true",
        help="List all available categories",
    )
    
    parser.add_argument(
        "--list-authors",
        action="store_true",
        help="List all authors in the collection",
    )
    
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Display collection statistics",
    )
    
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of quotes to display (default: 1)",
    )
    
    parser.add_argument(
        "--search",
        type=str,
        help="Search for quotes containing a keyword",
    )
    
    parser.add_argument(
        "--export",
        type=str,
        metavar="FILE",
        help="Export quotes to a JSON file",
    )
    
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored output",
    )

    args = parser.parse_args()

    try:
        generator = QuoteGenerator()
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Handle list categories
    if args.list_categories:
        print_header("Available Categories", args.no_color)
        categories = sorted(generator.get_categories())
        for category in categories:
            print(f"  • {category}")
        print()
        return

    # Handle list authors
    if args.list_authors:
        print_header("All Authors", args.no_color)
        authors = sorted(generator.get_all_authors())
        for author in authors:
            count = len(generator.get_quotes_by_author(author))
            print(f"  • {author} ({count} quote{'s' if count > 1 else ''})")
        print()
        return

    # Handle statistics
    if args.stats:
        stats = generator.get_statistics()
        print(format_statistics(stats, args.no_color))
        return

    # Handle search
    if args.search:
        results = generator.search_quotes(args.search)
        if results:
            print_header(f"Search Results for '{args.search}'", args.no_color)
            for quote in results:
                print(format_quote(quote, args.no_color))
        else:
            print(f"\nNo quotes found containing '{args.search}'\n")
        return

    # Handle export
    if args.export:
        try:
            generator.export_quotes(args.export, category=args.category)
            print(f"\n✓ Successfully exported quotes to {args.export}\n")
        except Exception as e:
            print(f"Error exporting quotes: {e}", file=sys.stderr)
            sys.exit(1)
        return

    # Handle author filter
    if args.author:
        quotes = generator.get_quotes_by_author(args.author)
        if quotes:
            print_header(f"Quotes by {args.author}", args.no_color)
            for quote in quotes[:args.count]:
                print(format_quote(quote, args.no_color))
        else:
            print(f"\nNo quotes found by author: {args.author}\n")
        return

    # Get random quote(s)
    if args.count > 1:
        quotes = generator.get_multiple_quotes(args.count, category=args.category)
        if quotes:
            for i, quote in enumerate(quotes, 1):
                if i > 1:
                    print()
                print(format_quote(quote, args.no_color))
        else:
            print(f"\nNo quotes found for category: {args.category}\n")
    else:
        quote = generator.get_random_quote(category=args.category)
        if quote:
            print(format_quote(quote, args.no_color))
        else:
            print(f"\nNo quotes found for category: {args.category}\n")


if __name__ == "__main__":
    main()
