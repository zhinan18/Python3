import logging; logging.basicConfig(level=logging.INFO)
import asyncio
from aiohttp import web
from models import User
import orm

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',
                        content_type='text/html', charset='UTF-8')


@asyncio.coroutine
def init(custom_loop):
    app = web.Application(loop=custom_loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


def test():
    yield from orm.create_pool(user='root', password='werered', database='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    yield from u.save()


test()
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
