"""
Output formatting utilities for the quotes generator.
"""

from typing import Dict


class Colors:
    """ANSI color codes for terminal output."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def format_quote(quote: Dict[str, str], no_color: bool = False) -> str:
    """
    Format a quote for display.
    
    Args:
        quote: Quote dictionary with text, author, and category.
        no_color: If True, disable colored output.
        
    Returns:
        Formatted quote string.
    """
    if no_color:
        return f'\n"{quote["text"]}\n  — {quote["author"]}\n  [{quote.get("category", "uncategorized")}]\n'
    
    text = f'{Colors.CYAN}"{quote["text"]}"{Colors.END}'
    author = f'{Colors.BOLD}— {quote["author"]}{Colors.END}'
    category = f'{Colors.YELLOW}[{quote.get("category", "uncategorized")}]{Colors.END}'
    
    return f'\n{text}\n  {author}\n  {category}\n'


def format_statistics(stats: Dict, no_color: bool = False) -> str:
    """
    Format statistics for display.
    
    Args:
        stats: Statistics dictionary from generator.
        no_color: If True, disable colored output.
        
    Returns:
        Formatted statistics string.
    """
    lines = []
    
    if not no_color:
        lines.append(f'\n{Colors.BOLD}{Colors.HEADER}📊 Quote Collection Statistics{Colors.END}\n')
    else:
        lines.append('\n📊 Quote Collection Statistics\n')
    
    lines.append(f"Total Quotes: {stats['total_quotes']}")
    lines.append(f"Total Categories: {stats['total_categories']}")
    lines.append(f"Total Authors: {stats['total_authors']}")
    lines.append(f"Average Quote Length: {stats['average_quote_length']:.0f} characters")
    
    lines.append("\nTop Categories:")
    for category, count in sorted(stats['categories'].items(), key=lambda x: x[1], reverse=True):
        lines.append(f"  • {category}: {count}")
    
    lines.append("\nTop Authors:")
    for author, count in stats['top_authors'].items():
        lines.append(f"  • {author}: {count}")
    
    lines.append("")
    return "\n".join(lines)


def print_header(text: str, no_color: bool = False) -> None:
    """
    Print a formatted header.
    
    Args:
        text: Header text.
        no_color: If True, disable colored output.
    """
    if no_color:
        print(f"\n{text}\n{'=' * len(text)}")
    else:
        print(f"\n{Colors.BOLD}{Colors.HEADER}{text}{Colors.END}\n{'=' * len(text)}")
