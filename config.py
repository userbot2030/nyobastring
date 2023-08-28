from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = getenv("OWNER_ID", "")
MUST_JOIN = getenv("MUST_JOIN", "")
SUPPORT = getenv("SUPPORT", "")
MONGO_URL = getenv("MONGO_URL", "")
JOIN1 = getenv("JOIN1", "")
JOIN2 = getenv("JOIN2", "")
JOIN3 = getenv("JOIN3", "")
JOIN4 = getenv("JOIN4", "")


if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")