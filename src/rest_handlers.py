import logging

from aiohttp import web

from . import cam_client

async def nvrtotg(request):
    params = request.rel_url.query

    chat_id = request.app['chat_id']
    tg = request.app['tg']
    cam_auth = request.app['cam_auth']

    cam = params.get('cam')
    port = params.get('port', 9786)
    host = params.get('host')
    text = params.get('text')
    logging.info('get request to proxy cam %s %s %s with text: %s', host, port, cam, text)

    photo = cam_client.get_image(host=host, port=port, cam=cam, auth=cam_auth)
    tg.send_photo(chat_id, photo, caption=text)

    return web.json_response('send to tg')
