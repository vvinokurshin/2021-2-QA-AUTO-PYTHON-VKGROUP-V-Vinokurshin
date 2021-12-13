import pytest

from mysql.client import MySQLClient

def pytest_configure(config):
    mysql_client = MySQLClient(user='root', password='pass', db_name='TEST_SQL')

    if not hasattr(config, 'workerinput'):
        mysql_client.recreate_db()
    
    mysql_client.connect(db_created=True)
    
    if not hasattr(config, 'workerinput'):
        mysql_client.create_tables()

    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request):
    client = request.config.mysql_client
    yield client
    client.connection.close()