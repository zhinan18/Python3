import orm
from models import User, Blog, Comment
import asyncio
from config import configs


@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop, host='127.0.0.1',user="root",password='werered',db='awesome')
    users = yield from User.findAll('email=?', 'test@example.com')
    if users:
        for user in users:
            yield from user.remove()
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    yield from u.save()




print('1')
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
