
import feedparser

# Création d'une instance
news_feed = feedparser.parse('https://www.greenpeace.fr/post_news/feed')

# Propriétés du flux
print(news_feed.feed.keys())

# Titre du flux
print("Feed Title:", news_feed.feed.title) 

# Sous-titre du flux
print("Feed Subtitle:", news_feed.feed.subtitle)

# Propriétés de chaque item du flux
print(news_feed.entries[0].keys())
    
# Récupération du deernier feed (dernier bulletin CERT-FR)
for i in range(0, len(news_feed.entries)):
        print(news_feed.entries[i]['title'])
        print(news_feed.entries[i]['link'])
