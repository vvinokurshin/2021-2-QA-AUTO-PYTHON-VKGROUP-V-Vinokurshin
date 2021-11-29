import json

from _pytest.compat import assert_never

from client.http_client import HttpClient
from base import BaseCase
from utils.fixtures import *


@pytest.mark.SOCKET
class TestMock(BaseCase):

    def test_get_non_existent_user(self):
        name = 'Valera'
        http_client = HttpClient()
        http_client.connect()
        result = http_client.get(name)

        assert result[0] == 'HTTP/1.0 404 NOT FOUND'
    

    def test_delete_non_exist(self):
        name = 'Valera'
        http_client = HttpClient()
        http_client.connect()
        result = http_client.delete(name)
        http_client.close()

        assert result[0] == 'HTTP/1.0 404 NOT FOUND'

    
    def test_post(self, http_client):
        params = 'Valera/Ololo'
        name = 'Valera'
        http_client.post(params)
        result = http_client.get(name)

        assert json.loads(result[-1]) == {'Valera': 'Ololo'}


    def test_put(self, create_user):
        name = 'Valera'
        params = 'Valera/Vinokurshin'
        create_user
        http_client = HttpClient()
        http_client.connect()
        http_client.put(params)
        result = http_client.get(name)
        http_client.close()

        assert json.loads(result[-1]) == {'Valera': 'Vinokurshin'}


    def test_delete(self, create_user):
        params = 'Valera/Vinokurshin'
        name = 'Valera'
        http_client = HttpClient()
        http_client.connect()
        http_client.put(params)
        http_client.delete(name)
        result = http_client.get(name)
        http_client.close()

        assert json.loads(result[0]) == { 'Valera': 'Vinokurshin' }

