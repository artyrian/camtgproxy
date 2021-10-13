import requests


def get_image(host, port, cam, auth):
    url = '{host}:{port}/cameras/{cam}/image?authorization={auth}=&keep_aspect_ratio=0&resolution=640x480'.format(
        host=host,
        port=port,
        cam=cam,
        auth=auth,
    )
    r = requests.get(url)
    return r.content
