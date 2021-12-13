import pytest
from utils.builder import MySQLBuilder

class MySQLBase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql = mysql_client

    @pytest.fixture(scope='session', autouse=True)
    def setup_data(self, mysql_client):
        self.mysql_builder = MySQLBuilder(mysql_client, 'access.log')
        self.prepare()

    def get_query(self, query_type):
        rows = self.mysql.session.query(query_type)
        return rows