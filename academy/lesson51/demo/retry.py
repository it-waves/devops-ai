import logging
import time
import requests
logging.basicConfig(level="INFO", format="%(levelname)s %(message)s")
URL = "http://127.0.0.1:8081/flaky"
for attempt in range(1, 5):
    try:
        r = requests.get(URL, timeout=5)
        r.raise_for_status()
        logging.info("attempt %d ok", attempt)
        break
    except requests.RequestException:
        logging.warning("attempt %d failed", attempt)
        time.sleep(2 ** (attempt - 1))
else:
    raise SystemExit("gave up: server still failing")
