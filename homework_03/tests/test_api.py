import pytest

from api.client import InvalidLoginException
from tests.base import ApiBase


class TestApi(ApiBase):

    def test_valid_login(self):
        self.api_client.post_login()

    # def test_create_segment(self, segment):
    #     self.api_client.post_create_segment(segment)
