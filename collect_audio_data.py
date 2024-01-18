import feedparser

def collect_episode_urls(rss_feed):

    feed = feedparser.parse(rss_feed)

    episode_urls = []

    for entry in feed.entries:

        episode_urls.append(entry.media_content[0]['url'])

        # print("Episode Title:", entry.title)
        # print("Episode Description:", entry.summary)
        # print("Episode Publish Date:", entry.published)
        # print("Episode Audio URL:", entry.media_content[0]['url'])
        # print("\n")

    return episode_urls