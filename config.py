from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "26477680"))
API_HASH = getenv("API_HASH", "b0d8504752cc1ecf52009ece2bdef0b8")
BOT_TOKEN = getenv("BOT_TOKEN", "6621888094:AAFiXgDSPC2PwFnlU_AqFptimOser6AuJmE")
OWNER_ID = getenv("OWNER_ID", "5779185981")
MUST_JOIN = getenv("MUST_JOIN", "Disney_storeDan")
SUPPORT = getenv("SUPPORT", "musik_suppotrdan")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://dan2:12345@cluster0.i1f6zo2.mongodb.net/?retryWrites=true&w=majority")
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
