import pytest

from tests.base import ApiBase

@pytest.mark.API
class TestApi(ApiBase):

    @pytest.fixture(scope='function')
    def test_valid_login(self):
        self.api_client.post_login()

    def test_create_segment(self, segment, test_valid_login):
        self.api_client.post_create_segment(segment)

