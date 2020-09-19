import feedparser

# provided endpoint num 1: https://rss.art19.com/the-daily

'''
Going with helper functions instead of Classes
and methods for simplicity. Goal is to get the
information ASAP with limited time. 
'''

def parse(url):
    '''
    Function parses info from URL
    '''
    return feedparser.parse(url)

def get_source(parsed):
    '''
    Takes parsed feed from "parse()"
    and gets info from it.  
    '''
    feed = parsed['feed']
    return {
        'title': feed['title'],
        'link': feed['link']
    }

def get_articles(parsed):
    '''
    Returns list of articles from 
    parsed feed.
    '''
    articles = []
    entries = parsed['entries']
    for entry in entries:
        articles.append({
            'id': entry['id'],
            'title': entry['title'],
            'summary': entry['summary']
            'link': entry['link'],
            'published': entry['published_parsed']
        })
    return articles
