'''
Tests
'''
def test_ping(app):
    '''
    Test ping handler, example
    '''
    res = app.test_client.get('/ping', gather_request=False)
    assert res.status == 200

def test_version(app):
    '''
    Test version handler, example
    '''
    res = app.test_client.get('/version', gather_request=False)
    assert res.status == 200

def test_proc(app):
    '''
    Test proc handler, example
    '''
    assert True
