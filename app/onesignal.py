import requests
import os

APP_ID = os.getenv("ONESIGNAL_APP_ID")

API_KEY = os.getenv("ONESIGNAL_API_KEY")

def send(news):

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
      "en": news.description,
      "fr": news.description
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
    raise RuntimeError(
      f"OneSignal did not create a message: {data}"
    )

  return data