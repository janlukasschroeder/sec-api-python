import requests

query_api_endpoint = "https://api.sec-api.io"
full_text_search_api_endpoint = "https://api.sec-api.io/full-text-search"
render_api_endpoint = "https://api.sec-api.io/filing-reader"


class QueryApi:
    """
    Base class for Query API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = query_api_endpoint + "?token=" + api_key

    def get_filings(self, query):
        response = requests.post(self.api_endpoint, json=query)
        return response.json()


class FullTextSearchApi:
    """
    Base class for Full-Text Search API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = full_text_search_api_endpoint + "?token=" + api_key

    def get_filings(self, query):
        response = requests.post(self.api_endpoint, json=query)
        return response.json()


class RenderApi:
    """
    Base class for Render API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = render_api_endpoint + "?token=" + api_key

    def get_filing(self, url):
        _url = self.api_endpoint + "&type=html&url=" + url
        response = requests.get(_url)
        return response.text
