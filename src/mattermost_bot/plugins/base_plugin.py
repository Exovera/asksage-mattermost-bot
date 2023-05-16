from os import environ

from mmpy_bot import Plugin
from redis import Redis

from src.askSage.sage_client import SageAPI


class SagePluginBase(Plugin):
    def __init__(self):
        super().__init__()
        self.sage_connection = SageAPI(
            environ.get("SAGE_EMAIL_ACCOUNT"),
            environ.get("SAGE_API_PASSWORD"),
            "https://user-server.asksage.ai/get-token",
            "https://server.asksage.ai",
            "https://server.asksage.ai/train",
        )
        self.redis = Redis.from_url(environ.get('REDIS_URL'))
