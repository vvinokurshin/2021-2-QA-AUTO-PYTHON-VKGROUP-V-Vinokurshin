import logging
from urllib.parse import urljoin

import requests

logger = logging.getLogger('test')

class InvalidLoginException(Exception):
    pass


class ApiClient:

    def __init__(self, url, user, password):
        self.session = requests.Session()
        self.base_url = url
        self.user = user
        self.password = password

        self.csrf_token = None
        self.sessionid_gtp = None

    def _request(self, method, url=None, params=None, location=None, headers=None,
                 data=None, json=None):

        if location:
            url = urljoin(self.base_url, location)
    
        response = self.session.request(method=method, url=url,
                                        headers=headers, params=params,
                                        data=data)

        if json:
            return response.json()
        return response

    def get_token(self):
        headers = {
            'Referer':
                'https://target.my.com/auth/mycom?state=target_login%3D1'
        }
        self._request(method='GET', location='csrf', headers=headers)
        return self.session.cookies.get('csrftoken')


    def post_login(self):
        url = 'https://auth-ac.my.com/auth'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'
        }


        data = {
            'email': self.user,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_'
                        'login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }

        self._request(method='POST', url=url, data=data, headers=headers)
        self.csrf_token = self.get_token()


    def post_create_segment(self, title):
        location = 'api/v2/remarketing/segments.json'

        params = {"fields": "relations__object_type,relations__object_id,"
                            "relations__params,relations_count,id,name,"
                            "pass_condition,created,campaign_ids,users,flags"
                  }

        data = {
            'name': title,
            'pass_condition': 1,
            'relations': [
                {
                    'object_type': "remarketing_player",
                    'params': {
                        'type': "positive",
                        'left': 365,
                        'right': 0
                    }
                }
            ]
        }

        headers = {
            "Content-Type": "application/json",
            'X-CSRFToken': self.csrf_token
        }
        response = self._request(method="POST", location=location, 
                                 headers=headers, json=data)
        return response.get('id')
    
