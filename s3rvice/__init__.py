'''
Core
'''
from concurrent.futures import ThreadPoolExecutor as Pool

from sanic import Sanic
from sanic.response import json

from .handlers import system, process
from .model import Model

application = Sanic(__name__)


@application.listener('before_server_start')
async def bootstrap_server(app, loop):  # pragma: no cover
    '''
    Preload stuff
    '''

    with open('VERSION', 'r') as f:
        app.VERSION = f.read()

    app.model = Model()
    app.executor = Pool(max_workers=10)


application.add_route(system.ping, '/ping', methods=['GET'])
application.add_route(system.version, '/version', methods=['GET'])
application.add_route(process.process, '/proc', methods=['POST'])
