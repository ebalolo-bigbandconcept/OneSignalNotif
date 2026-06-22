import time
import logging

from feeds import get_feed
from storage import (
  is_sent,
  mark_sent
)
from onesignal import send
from utils import html_to_text

logger = logging.getLogger(__name__)

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
    item.description = html_to_text(item.content_html)[:150]
    result = send(item)
    mark_sent(item.id)

    logger.info(f"Sent: {item.title} ({result['id']})")

    # Petit délai entre deux envois.
    time.sleep(SEND_DELAY_SECONDS)