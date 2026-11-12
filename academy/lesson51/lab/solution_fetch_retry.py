import logging
import os
import sys
import time

import requests

logging.basicConfig(level="INFO", format="%(levelname)s %(message)s")
BASE = os.getenv("API_URL", "http://127.0.0.1:8081")
for attempt in range(1, 5):
    try:
        r = requests.get(BASE + "/flaky", timeout=2)
        r.raise_for_status()
        logging.info("attempt %d ok", attempt)
        print(r.json()["status"])
        sys.exit(0)
    except requests.RequestException:
        logging.warning("attempt %d failed", attempt)
        time.sleep(2 ** (attempt - 1))
logging.error("gave up after 4 attempts")
sys.exit(1)
