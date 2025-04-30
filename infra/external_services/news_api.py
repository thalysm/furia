import feedparser

def get_latest_news():
    query = "FURIA esports"
    rss_url = f"https://news.google.com/rss/search?q={query.replace(' ', '+')}&hl=pt-BR&gl=BR&ceid=BR:pt-419"

    feed = feedparser.parse(rss_url)
    news_items = []

    for entry in feed.entries[:5]:  # Pegamos as 5 notícias mais recentes
        news_items.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        })

    return news_items
