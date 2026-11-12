import requests

URL = "http://127.0.0.1:8081/slow"
try:
    r = requests.get(URL, timeout=1)
    print("ok", r.status_code)
except requests.exceptions.Timeout:
    print("too slow: gave up after 1 second")
