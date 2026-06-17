import time
import os
from storage import init_db
from worker import process_feed

FEED_URL = os.getenv("FEED_URL")

INTERVAL = int(
  os.getenv(
    "CHECK_INTERVAL",
    "300"
  )
)


def main():
  init_db()

  while True:
    try:
      process_feed(FEED_URL)
      
    except Exception as e:
      print(e)

    time.sleep(INTERVAL)

if __name__ == "__main__":
  main()