# By < @xditya >
# // @BotzHub //

from telethon import TelegramClient
from telethon.sessions import StringSession
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = 9397588
API_HASH = "79d67b413fdc8065c9f914e05d83bd11"
SESSION = """1AZWarzYBu4qYMFR0BrdJzuNh2uIoSOG0OguCahSAzPuQsdfSrWUiMANNOBI0yhVvXYDm3IEq1ffQSsKaBIh0CbM18sxUBvhX8pwuejF9N3FGu_Yv0IBdWj0cWRthQOSysgDTZdvYS9FstXv1_rvrFHBI2XlyTq-dnidjiEkoOA_Kp-VU9LnWHjIUrX6QOIi7RMCT9G2p4CFivihq1UWzrX-3qj8_vSkbCYu04a92sa1Qoi1p9akF0rPUuzmoBgNNsVaC9WtkJxo6dZyzNqwMkTklbr1fmAUH486kmjJpVyL4c56M8uG1riuwH273KAOW-ju7tKsp5HYZmtVXSmL1tYG-y3GjGws="""

BotzHub = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
