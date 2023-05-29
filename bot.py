import env
import logging
from pyrogram import Client, idle
import time
import logging
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid


logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

StartTime = time.time()

app = Client(
    "Naya",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    bot_token=env.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="Naya"),
)


if __name__ == "__main__":
    logging.info("Starting the bot")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.me.username
    logging.info(f"@{uname} is now running!")
    idle()
    app.stop()
    logging.info("Bot stopped. Alvida!")
