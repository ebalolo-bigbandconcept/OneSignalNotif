import requests
import os
from config import logger

APP_ID = os.getenv("ONESIGNAL_APP_ID")
API_KEY = os.getenv("ONESIGNAL_API_KEY")

def send(news):
  description = (
        getattr(news, "description", "") or
        "Nouvel article disponible. "
        "Cliquez pour en savoir plus..."
    )
  
  payload = {
    "app_id": APP_ID,
    "target_channel": "push",
    "included_segments": [
      "Total Subscriptions"
    ],
    "name": news.title,
    "headings": {
      "en": news.title,
      "fr": news.title
    },
    "contents": {
      "en": description,
      "fr": description
    },
    "url": news.url
  }

  headers = {
    "Authorization": f"Key {API_KEY}",
    "Content-Type": "application/json"
  }

  response = requests.post(
    "https://api.onesignal.com/notifications?c=push",
    json=payload,
    headers=headers,
    timeout=30
  )

  response.raise_for_status()

  data = response.json()

  if not data.get("id"):
    logger.error(f"Failed to send notification for {news.title}")
    raise RuntimeError(
      f"OneSignal did not create a message: {data}"
    )

  return data