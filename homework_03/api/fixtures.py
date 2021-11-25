import pytest

from api.client import ApiClient

@pytest.fixture(scope='session')
def cookies(credentials):
    api_client = ApiClient(*credentials)
    api_client.post_login()

    cookies_list = []
    for cookie in api_client.session.cookies:
        cookie_dict = {'domain': cookie.domain,
                       'name': cookie.name,
                       'value': cookie.value,
                       'secure': cookie.secure
                       }
        cookies_list.append(cookie_dict)

    return cookies_list