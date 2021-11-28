import pytest

from utils.builder import Builder


class ApiBase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client, logger):
        self.api_client = api_client
        self.builder = Builder()
        self.logger = logger

        if self.authorize:
            self.api_client.post_login()

    @pytest.fixture()
    def segment(self):
        segment_name = self.builder.segment()

        return segment_name


    def create_segment(self, title):
        return self.api_client.post_segment_create(title=title)

