import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

current_date = datetime.now().strftime("%Y-%m-%d")

logging.info("Поточна дата: %s", current_date)
