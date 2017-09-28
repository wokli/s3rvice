'''
System handlers
'''
from sanic.response import json, text

async def ping(_): # pragma: no cover
    '''
    Ping handler
    '''
    return json({'status': 'OK'})

async def version(req): # pragma: no cover
    '''
    Version handler
    '''
    return text(req.app.VERSION)
