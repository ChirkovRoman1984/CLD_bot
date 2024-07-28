import json
import logging
import os

from aiogram import Bot, Dispatcher, types

from app.handlers import register_all_handlers

# Logger initialization and logging level setting
log = logging.getLogger(__name__)
log.setLevel(os.environ.get('LOGGING_LEVEL', 'INFO').upper())

bot = Bot(os.environ.get('TOKEN'))
dp = Dispatcher(bot)
register_all_handlers(dp)


async def process_event(update):
    """
    Converting an Yandex.Cloud functions event to an update and
    handling tha update.
    """

    # update = json.loads(event['body'])
    log.debug('Update: ' + str(update))

    Bot.set_current(dp.bot)
    update = types.Update.to_object(update)
    await dp.process_update(update)


async def handler(event, _):  # async def handler(event, context):
    """Yandex.Cloud functions handler."""

    for message in event["messages"]:
        update = json.loads(message["details"]["message"]["body"])
        await process_event(update)
