# Usage Examples

Comprehensive examples for using the Random Quotes Generator in various scenarios.

## Table of Contents

- [Basic Examples](#basic-examples)
- [CLI Examples](#cli-examples)
- [Python Integration](#python-integration)
- [Real-World Use Cases](#real-world-use-cases)

## Basic Examples

### Get a Random Quote

```python
from quotes_generator import QuoteGenerator

generator = QuoteGenerator()
quote = generator.get_random_quote()

print(f'"{quote["text"]}"')
print(f"— {quote['author']}")
```

### Filter by Category

```python
# Get a motivational quote
motivational = generator.get_random_quote(category="motivation")

# Get a wisdom quote
wisdom = generator.get_random_quote(category="wisdom")

# Get multiple success quotes
success_quotes = generator.get_multiple_quotes(3, category="success")
```

### Search by Author

```python
# Get all quotes by Steve Jobs
jobs_quotes = generator.get_quotes_by_author("Steve Jobs")

for quote in jobs_quotes:
    print(f"• {quote['text']}")
```

## CLI Examples

### Basic Commands

```bash
# Random quote
quotes

# Category-specific
quotes --category motivation

# Multiple quotes
quotes --count 5

# Search by author
quotes --author "Einstein"
```

### Advanced Commands

```bash
# Search for keywords
quotes --search "success"

# View statistics
quotes --stats

# List all categories
quotes --list-categories

# Export to file
quotes --export my_quotes.json --category wisdom

# Disable colors
quotes --no-color
```

## Python Integration

### Daily Quote Script

```python
#!/usr/bin/env python3
"""Daily motivation quote script."""

from quotes_generator import QuoteGenerator
from datetime import datetime

def get_daily_quote():
    generator = QuoteGenerator()
    quote = generator.get_random_quote(category="motivation")
    
    today = datetime.now().strftime("%A, %B %d, %Y")
    
    print(f"\n{'='*60}")
    print(f"Daily Motivation - {today}")
    print(f"{'='*60}\n")
    print(f'"{quote["text"]}"')
    print(f"\n— {quote['author']}")
    print(f"[{quote['category']}]\n")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    get_daily_quote()
```

### Quote of the Day API

```python
from flask import Flask, jsonify
from quotes_generator import QuoteGenerator

app = Flask(__name__)
generator = QuoteGenerator()

@app.route('/api/quote')
def random_quote():
    quote = generator.get_random_quote()
    return jsonify(quote)

@app.route('/api/quote/<category>')
def category_quote(category):
    quote = generator.get_random_quote(category=category)
    if quote:
        return jsonify(quote)
    return jsonify({"error": "Category not found"}), 404

@app.route('/api/categories')
def categories():
    return jsonify(list(generator.get_categories()))

if __name__ == '__main__':
    app.run(debug=True)
```

### Discord Bot Integration

```python
import discord
from quotes_generator import QuoteGenerator

client = discord.Client()
generator = QuoteGenerator()

@client.event
async def on_message(message):
    if message.content.startswith('!quote'):
        quote = generator.get_random_quote()
        
        embed = discord.Embed(
            title="💭 Inspirational Quote",
            description=f'"{quote["text"]}"',
            color=0x00ff00
        )
        embed.add_field(name="Author", value=quote["author"])
        embed.add_field(name="Category", value=quote["category"])
        
        await message.channel.send(embed=embed)
    
    elif message.content.startswith('!motivate'):
        quote = generator.get_random_quote(category="motivation")
        await message.channel.send(
            f'🌟 {quote["text"]} — {quote["author"]}'
        )

client.run('YOUR_BOT_TOKEN')
```

### Slack Bot

```python
from slack_sdk import WebClient
from quotes_generator import QuoteGenerator
import schedule
import time

client = WebClient(token="YOUR_SLACK_TOKEN")
generator = QuoteGenerator()

def post_daily_quote():
    quote = generator.get_random_quote(category="motivation")
    
    message = f"""
    :star2: *Daily Motivation* :star2:
    
    _{quote['text']}_
    
    — {quote['author']}
    """
    
    client.chat_postMessage(
        channel="#general",
        text=message
    )

# Schedule daily at 9 AM
schedule.every().day.at("09:00").do(post_daily_quote)

while True:
    schedule.run_pending()
    time.sleep(60)
```

### Twitter Bot

```python
import tweepy
from quotes_generator import QuoteGenerator
import schedule
import time

# Twitter API credentials
auth = tweepy.OAuthHandler("API_KEY", "API_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_SECRET")
api = tweepy.API(auth)

generator = QuoteGenerator()

def tweet_quote():
    quote = generator.get_random_quote()
    
    # Format tweet (max 280 characters)
    tweet = f'"{quote["text"]}" — {quote["author"]} #{quote["category"]}'
    
    if len(tweet) <= 280:
        api.update_status(tweet)
        print(f"Tweeted: {tweet}")
    else:
        print("Quote too long for Twitter")

# Tweet every 4 hours
schedule.every(4).hours.do(tweet_quote)

while True:
    schedule.run_pending()
    time.sleep(60)
```

### Email Newsletter

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from quotes_generator import QuoteGenerator

def send_quote_newsletter(recipients):
    generator = QuoteGenerator()
    quote = generator.get_random_quote()
    
    # Email content
    html = f"""
    <html>
      <body style="font-family: Arial, sans-serif;">
        <h2 style="color: #2c3e50;">Daily Inspiration</h2>
        <blockquote style="font-size: 18px; font-style: italic; color: #34495e;">
          "{quote['text']}"
        </blockquote>
        <p style="text-align: right; color: #7f8c8d;">
          — {quote['author']}
        </p>
        <p style="color: #95a5a6; font-size: 12px;">
          Category: {quote['category']}
        </p>
      </body>
    </html>
    """
    
    # Send email
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Your Daily Inspiration"
    msg['From'] = "quotes@example.com"
    
    html_part = MIMEText(html, 'html')
    msg.attach(html_part)
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login("your_email@gmail.com", "your_password")
        
        for recipient in recipients:
            msg['To'] = recipient
            server.send_message(msg)
```

### Terminal Startup Message

Add to your `.bashrc` or `.zshrc`:

```bash
# Add to ~/.bashrc or ~/.zshrc
python -m quotes_generator --category motivation
```

Or create a custom script:

```python
#!/usr/bin/env python3
"""Terminal startup quote."""

from quotes_generator import QuoteGenerator
import random

def startup_quote():
    generator = QuoteGenerator()
    
    # Random category or specific one
    categories = ["motivation", "wisdom", "success"]
    category = random.choice(categories)
    
    quote = generator.get_random_quote(category=category)
    
    print("\n" + "="*70)
    print(f"  {quote['text']}")
    print(f"  — {quote['author']}")
    print("="*70 + "\n")

if __name__ == "__main__":
    startup_quote()
```

### Quote Analytics Dashboard

```python
from quotes_generator import QuoteGenerator
import matplotlib.pyplot as plt

def create_analytics_dashboard():
    generator = QuoteGenerator()
    stats = generator.get_statistics()
    
    # Category distribution
    categories = stats['categories']
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.bar(categories.keys(), categories.values())
    plt.title('Quotes by Category')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Number of Quotes')
    
    # Top authors
    plt.subplot(1, 2, 2)
    authors = stats['top_authors']
    plt.barh(list(authors.keys()), list(authors.values()))
    plt.title('Top Authors')
    plt.xlabel('Number of Quotes')
    
    plt.tight_layout()
    plt.savefig('quote_analytics.png')
    print("Analytics dashboard saved to quote_analytics.png")

if __name__ == "__main__":
    create_analytics_dashboard()
```

### Custom Quote Recommender

```python
from quotes_generator import QuoteGenerator
import random

class QuoteRecommender:
    def __init__(self):
        self.generator = QuoteGenerator()
        self.user_preferences = {}
    
    def recommend_by_mood(self, mood):
        """Recommend quotes based on user mood."""
        mood_map = {
            "happy": ["motivation", "success", "inspiration"],
            "sad": ["wisdom", "perseverance", "courage"],
            "stressed": ["life", "wisdom", "action"],
            "motivated": ["success", "achievement", "ambition"],
            "thoughtful": ["wisdom", "purpose", "values"]
        }
        
        categories = mood_map.get(mood.lower(), ["motivation"])
        category = random.choice(categories)
        
        return self.generator.get_random_quote(category=category)
    
    def recommend_by_time(self):
        """Recommend quotes based on time of day."""
        from datetime import datetime
        hour = datetime.now().hour
        
        if 5 <= hour < 12:
            category = "motivation"  # Morning motivation
        elif 12 <= hour < 17:
            category = "action"  # Afternoon action
        elif 17 <= hour < 21:
            category = "wisdom"  # Evening reflection
        else:
            category = "life"  # Night contemplation
        
        return self.generator.get_random_quote(category=category)

# Usage
recommender = QuoteRecommender()

# Get quote based on mood
quote = recommender.recommend_by_mood("motivated")
print(f'"{quote["text"]}" — {quote["author"]}')

# Get quote based on time
quote = recommender.recommend_by_time()
print(f'"{quote["text"]}" — {quote["author"]}')
```

## Real-World Use Cases

### 1. Productivity App
Integrate motivational quotes into your productivity application to inspire users.

### 2. Learning Platform
Display relevant quotes on course pages to motivate learners.

### 3. Meditation App
Show wisdom quotes during meditation sessions.

### 4. Fitness App
Display motivational quotes to encourage workout completion.

### 5. Corporate Dashboard
Show daily inspiration on company dashboards or intranets.

### 6. Educational Tools
Use quotes in presentations, assignments, or learning materials.

### 7. Social Media Management
Automate inspirational content posting across platforms.

### 8. Personal Development Journal
Include daily quotes in digital or physical journals.

For more examples, check the `examples/` directory in the repository.
