from prometheus_client import Gauge, start_http_server
import requests
import time

CONFIDENCE = Gauge(
    "prediction_confidence_score",
    "Latest prediction confidence"
)

APP_URL = "http://16.16.226.86:32500/api/latest-confidence"

def get_confidence():
    try:
        r = requests.get(APP_URL, timeout=5)

        if r.status_code == 200:
            return float(
                r.json().get("confidence", 1.0)
            )
    except Exception:
        pass

    return 1.0

if __name__ == "__main__":

    start_http_server(8000)

    while True:

        value = get_confidence()

        CONFIDENCE.set(value)

        time.sleep(5)