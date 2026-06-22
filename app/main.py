import time
import os
import logging
from storage import init_db
from worker import process_feed

# Configuration de base du logging.
logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s - %(levelname)s: %(message)s"
)

# URL du flux à surveiller.
FEED_URL = os.getenv("FEED_URL")

# Intervalle entre deux vérifications du flux.
INTERVAL = int(
  os.getenv(
    "CHECK_INTERVAL",
    "300"
  )
)


def main():
  # Prépare la base avant de lancer la boucle.
  init_db()

  # Boucle infinie de surveillance du flux.
  while True:
    try:
      process_feed(FEED_URL)

    except Exception as e:
      logging.error(e)

    # Pause avant le prochain passage.
    time.sleep(INTERVAL)

if __name__ == "__main__":
  main()