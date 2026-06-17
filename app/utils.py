import re

def html_to_text(html: str) -> str:
  return re.sub(
    "<[^<]+?>",
    "",
    html
  ).strip()