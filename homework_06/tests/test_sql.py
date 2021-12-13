import pytest
from tests.base import MySQLBase

from mysql.models import *
from answers import *

@pytest.mark.SQL
class TestSQL(MySQLBase):

    f = open('res_python.txt', 'r')

    def prepare(self):
        self.mysql_builder.total_count()
        self.mysql_builder.count_by_type()
        self.mysql_builder.top10_request_by_count()
        self.mysql_builder.top5_4XX_by_size()
        self.mysql_builder.top5_users_5XX_by_count()

    def get_count_lines(self):
        line = self.f.readline()
        count = 0

        while line[0] != '\n':
            count += 1
            line = self.f.readline()

        return count - 1 # -1 возвращаем, так как заголовок не считаем


    def test_total_count(self):
        result = self.get_query(TotalCount)

        assert len(result.all()) == self.get_count_lines()


    def test_count_by_type(self):
        result = self.get_query(CountByType)

        assert len(result.all()) == self.get_count_lines()


    def test_top10_request_by_count(self):
        result = self.get_query(Top10_request_by_count)

        assert len(result.all()) == self.get_count_lines()


    def test_top5_4XX_by_size(self):
        result = self.get_query(Top5_4XX_by_size)

        assert len(result.all()) == self.get_count_lines()


    def test_top5_users_5XX_by_count(self):
        result = self.get_query(Top5_users_5XX_by_count)

        assert len(result.all()) == self.get_count_lines()
