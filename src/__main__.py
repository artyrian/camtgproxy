import configargparse
import logging
import os

import asyncio

import telegram

from aiohttp import web
from aiomisc.log import basic_config, LogFormat


from . import rest_handlers


def main():
    script_dir = os.path.dirname(__file__)
    default_config = os.path.join(script_dir, 'cfg', 'default.conf')
    parser = configargparse.ArgParser(default_config_files=[default_config])
    parser.add_argument('-c', required=False, is_config_file=True, help='config file path')
    parser.add_argument('--port', help='Port for server to run')
    parser.add_argument('--tg-token')
    parser.add_argument('--chat-id')
    parser.add_argument('--cam-auth')
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_web_app(chat_id=args.chat_id,
                                               tg_token=args.tg_token,
                                               cam_auth=args.cam_auth))
    web.run_app(app, port=args.port, access_log=None)


async def init_web_app(chat_id, tg_token, cam_auth):
    app = web.Application()
    app['tg'] = telegram.Bot(token=tg_token)
    app['chat_id'] = chat_id
    app['cam_auth'] = cam_auth

    app.router.add_post('/nvrtotg', rest_handlers.nvrtotg)
    return app


if __name__ == '__main__':
    basic_config(level=logging.INFO, log_format=LogFormat.stream, buffered=True)
    main()
