import requests

query_api_endpoint = 'https://api.sec-api.io'


class QueryApi:
    """
    Base class for Query API
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = query_api_endpoint + '?token=' + api_key

    def get_filings(self, query):
        response = requests.post(self.api_endpoint, json=query)
        return response.json()
