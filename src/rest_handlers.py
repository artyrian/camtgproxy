from . import cam_client

from aiohttp import web


async def nvrtotg(request):
    params = request.rel_url.query

    chat_id = request.app['chat_id']
    tg = request.app['tg']
    cam_auth = request.app['cam_auth']

    cam = params.get('cam')
    port = params.get('port', 9786)
    host = params.get('host')
    text = params.get('text')

    photo = cam_client.get_image(host=host, port=port, cam=cam, auth=cam_auth)
    tg.send_message(chat_id, text)
    tg.send_photo(chat_id, photo)

    return web.json_response('send to tg')
