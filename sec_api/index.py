import requests
import json
import re

query_api_endpoint = "https://api.sec-api.io"
full_text_search_api_endpoint = "https://api.sec-api.io/full-text-search"
render_api_endpoint = "https://archive.sec-api.io"
xbrl_api_endpoint = "https://api.sec-api.io/xbrl-to-json"
extractor_api_endpoint = "https://api.sec-api.io/extractor"


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
        self.api_endpoint = render_api_endpoint

    def get_filing(self, url):
        filename = re.sub(r"https://www.sec.gov/Archives/edgar/data", "", url)
        _url = self.api_endpoint + filename + "?token=" + self.api_key
        response = requests.get(_url)
        return response.text


class XbrlApi:
    """
    Base class for XBRL-to-JSON API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = xbrl_api_endpoint + "?token=" + api_key

    def xbrl_to_json(self, htm_url="", xbrl_url="", accession_no=""):
        if len(htm_url) == 0 and len(xbrl_url) == 0 and len(accession_no) == 0:
            raise ValueError("htm_url, xbrl_url or accession_no must be present")

        _url = ""

        if len(htm_url):
            _url = self.api_endpoint + "&htm-url=" + htm_url

        if len(xbrl_url):
            _url = self.api_endpoint + "&xbrl-url=" + xbrl_url

        if len(accession_no):
            _url = self.api_endpoint + "&accession-no=" + accession_no

        response = requests.get(_url)
        return json.loads(response.text)


class ExtractorApi:
    """
    Base class for 10-K/10-Q item/section extractor API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = extractor_api_endpoint + "?token=" + api_key

    def get_section(self, filing_url="", section="1A", return_type="text"):
        if len(filing_url) == 0:
            raise ValueError("filing_url must be present")

        _url = (
            self.api_endpoint
            + "&url="
            + filing_url
            + "&item="
            + section
            + "&type="
            + return_type
        )

        response = requests.get(_url)
        return response.text
