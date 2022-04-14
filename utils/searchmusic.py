import json
from youtubesearchpython import VideosSearch


class YTSearch:
    def __init__(self, limit, queries):
        query = ""
        for item in queries:
            query += item
        Search = VideosSearch(query, limit=limit).result()
        dumps = json.dumps(Search)
        links = json.loads(dumps)
        self.results = links['result']

    def title(self):
        titles = []
        for result in self.results:
            titles.append(result['title'])
        print(titles)
        return titles

    def duration(self):
        duration = None
        for result in self.results:
            duration = result['accessibility']['duration']
        print(duration)
        return duration

    def url(self):
        url = None
        for result in self.results:
            url = result['link']
        return url


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)