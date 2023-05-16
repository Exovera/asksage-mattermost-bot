import logging
from os import environ

from mmpy_bot import Bot, Settings

from src.mattermost_bot.plugins.ask_plugin import SageQueryPlugin

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logger.info(f"Connecting to {environ.get('MATTERMOST_URL')} on port {8065}")
logger.info(f"Mattermost team: {environ.get('MATTERMOST_TEAM')}")


class MattermostBot:

    def __init__(self):
        self.bot = Bot(
            settings=Settings(
                MATTERMOST_URL=environ.get("MATTERMOST_URL"),
                MATTERMOST_PORT=8065,
                MATTERMOST_API_PATH='/api/v4',
                BOT_TOKEN=environ.get("MATTERMOST_BOT_TOKEN"),
                BOT_TEAM=environ.get("MATTERMOST_TEAM"),
                SSL_VERIFY=False,
            ),  # Either specify your settings here or as environment variables.
            plugins=[SageQueryPlugin()],
            # Add your own plugins here.
        )
        logger.info("Connected to MM")


logger.info("Connecting to MM")
sage_bot = MattermostBot()
sage_bot.bot.run()
