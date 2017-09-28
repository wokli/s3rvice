'''
Основной обработчик
'''
from sanic.response import json
from sanic.log import log


def _process(model, params): # pragma: no cover
    '''
    Запуск модели
    '''
    result = model.predict(params)

    return result


async def process(req): # pragma: no cover
    '''
    Await-обертка над process
    '''
    try:
        result = await req.app.loop.run_in_executor(
            req.app.executor,
            _process,
            req.app.model,
            req.json
        )

        return json({
            'result': result,
            'error': None,
            'success': True
        })
    except Exception as exc:
        log.exception('process error')
        return json({
            'success': False,
            'error': 'process error: {}'.format(exc),
            'result': None
        }, status=400)
