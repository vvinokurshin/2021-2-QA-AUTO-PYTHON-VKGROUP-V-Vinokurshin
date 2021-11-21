import pytest
from tests.base import MySQLBase

from mysql.models import *
from answers import *

@pytest.mark.SQL
class TestSQL(MySQLBase):

    def prepare(self):
        self.mysql_builder.total_count()
        self.mysql_builder.count_by_type()
        self.mysql_builder.top10_request_by_count()
        self.mysql_builder.top5_4XX_by_size()
        self.mysql_builder.top5_users_5XX_by_count()

    def test_total_count(self):
        result = self.get_query(TotalCount)

        assert len(result.all()) == 1
        assert result.first().count == TOTAL_COUNT


    def test_count_by_type(self):
        result = self.get_query(CountByType)

        assert len(result.all()) == 4
        for method in METHODS.keys():
            assert result.filter_by(type=method).first().count == METHODS.get(method)


    def test_top10_request_by_count(self):
        result = self.get_query(Top10_request_by_count)

        assert len(result.all()) == 10
        for url in URL.keys():
            assert result.filter_by(url=url).first().count == URL.get(url)


    def test_top5_4XX_by_size(self):
        result = self.get_query(Top5_4XX_by_size)

        assert len(result.all()) == 5
        for i in range(5):
            assert result.filter_by(url=REQESTS[i][3]).first().ip == REQESTS[i][0]
            assert result.filter_by(url=REQESTS[i][3]).first().rc == REQESTS[i][1]
            assert result.filter_by(url=REQESTS[i][3]).first().size == REQESTS[i][2]


    def test_top5_users_5XX_by_count(self):
        result = self.get_query(Top5_users_5XX_by_count)

        assert len(result.all()) == 5
        for ip in IP.keys():
            assert result.filter_by(ip=ip).first().count == IP.get(ip)

