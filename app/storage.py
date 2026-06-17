import sqlite3

DB_PATH = "/data/feed.db"

def init_db():
  conn = sqlite3.connect(DB_PATH)

  conn.execute("""
    CREATE TABLE IF NOT EXISTS sent_news(
      id TEXT PRIMARY KEY,
      sent_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
  """)

  conn.commit()
  conn.close()


def is_sent(news_id: str) -> bool:
  conn = sqlite3.connect(DB_PATH)

  row = conn.execute(
    "SELECT 1 FROM sent_news WHERE id=?",
    (news_id,)
  ).fetchone()

  conn.close()

  return row is not None


def mark_sent(news_id: str):
  conn = sqlite3.connect(DB_PATH)

  conn.execute(
    "INSERT INTO sent_news(id) VALUES(?)",
    (news_id,)
  )

  conn.commit()
  conn.close()