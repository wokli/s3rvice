'''
Entrypoint
'''
from . import application

if __name__ == '__main__': # pragma: no cover
    application.run(host="0.0.0.0", port=8000, log_config=None, workers=2)
