import time

from feeds import get_feed
from storage import (
  is_sent,
  mark_sent
)
from onesignal import send
from utils import html_to_text
from config import logger

SEND_DELAY_SECONDS = 60

def process_feed(feed_url):
  items = get_feed(feed_url)

  # On traite les éléments du plus ancien au plus récent.
  items.reverse()

  for item in items:
    # On ignore ce qui a déjà été envoyé.
    if is_sent(item.id):
      continue

    # On garde un résumé court pour la notification.
    item.description = build_description(item)
    result = send(item)
    mark_sent(item.id)

    logger.info(f"Sent: {item.title} ({result['id']})")

    # Petit délai entre deux envois.
    time.sleep(SEND_DELAY_SECONDS)

def build_description(item):
  # Tentative depuis le contenu HTML
    description = html_to_text(
        item.content_html or ""
    ).strip()

    # Fallback
    if not description:
        description = (
            "Nouvel article disponible. "
            "Cliquez pour en savoir plus..."
        )

    # Limite pour la notification
    return description[:150]