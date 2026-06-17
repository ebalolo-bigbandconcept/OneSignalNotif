from dataclasses import dataclass

@dataclass
class NewsItem:
  id: str
  title: str
  url: str
  content_html: str
  date_published: str