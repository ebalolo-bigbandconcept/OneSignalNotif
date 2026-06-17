import requests
from models import NewsItem

def get_feed(url: str) -> list[NewsItem]:
  response = requests.get(
    url,
    timeout=30
  )

  response.raise_for_status()

  data = response.json()

  items = []

  for item in data.get("items", []):
    items.append(
      NewsItem(
        id=item["id"],
        title=item["title"],
        url=item["url"],
        content_html=item.get(
          "content_html",
          ""
        ),
        date_published=item.get(
          "date_published",
          ""
        )
      )
    )

  return items