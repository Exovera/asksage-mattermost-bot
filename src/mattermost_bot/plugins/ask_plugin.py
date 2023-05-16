import logging

from mmpy_bot import Message, listen_to

from src.mattermost_bot.plugins.base_plugin import SagePluginBase

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

import asyncio
from concurrent.futures import ThreadPoolExecutor


class SageQueryPlugin(SagePluginBase):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.executor = ThreadPoolExecutor()

    @listen_to("=sage ask")
    async def respond(self, message: Message):
        channel_id = message.channel_id
        message_from = message.body.get('data').get('sender_name')
        logger.debug("Querying Sage")
        message = str(message.text.split('=sage ask')[1].strip())
        logger.debug(f"User's message: {message}")

        loop = asyncio.get_running_loop()
        response, messages = await loop.run_in_executor(
            self.executor, self._sage_query, message_from, message)

        logger.debug("Retrieved Sage Answer")
        sage_response = response.get('message')
        logger.debug(f"Responding: {sage_response}")
        self.driver.create_post(channel_id=channel_id, message=sage_response)

    def _sage_query(self, message_from, message):
        message = " ".join(message.split(' ')[1:])

        response = self.sage_connection.query_sage(message)
        messages = [{'user': message_from, 'message': message}]

        return response, messages
