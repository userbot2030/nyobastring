from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "22156937"))
API_HASH = getenv("API_HASH", "0f8f66b06b1c53b9263bcfb1123e9c85")
BOT_TOKEN = getenv("BOT_TOKEN", "5688352753:AAFAE75kCKzrkueAX3WPvPRi-H8BmZZavNs")

MUST_JOIN = getenv("MUST_JOIN", "kazusupportgrp")
MONGO_URL = getenv("MONGO_URL")


if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")