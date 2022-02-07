import requests
import json
import re
import time

query_api_endpoint = "https://api.sec-api.io"
full_text_search_api_endpoint = "https://api.sec-api.io/full-text-search"
render_api_endpoint = "https://archive.sec-api.io"
xbrl_api_endpoint = "https://api.sec-api.io/xbrl-to-json"
extractor_api_endpoint = "https://api.sec-api.io/extractor"
mapping_api_endpoint = "https://api.sec-api.io/mapping"


class QueryApi:
    """
    Base class for Query API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = query_api_endpoint + "?token=" + api_key

    def get_filings(self, query):
        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(self.api_endpoint, json=query)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                raise Exception("API error: " + response.status_code)
        else:
            # request failed
            raise Exception("API error")


class FullTextSearchApi:
    """
    Base class for Full-Text Search API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = full_text_search_api_endpoint + "?token=" + api_key

    def get_filings(self, query):
        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(self.api_endpoint, json=query)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                raise Exception("API error: " + response.status_code)
        else:
            # request failed
            raise Exception("API error")


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

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.get(_url)
            if response.status_code == 200:
                return response.text
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                raise Exception("API error: " + response.status_code)
        else:
            # request failed
            raise Exception("API error")


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

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.get(_url)
            if response.status_code == 200:
                data = json.loads(response.text)
                return data
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                raise Exception("API error: " + response.status_code)
        else:
            # request failed
            raise Exception("API error")


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

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.get(_url)
            if response.status_code == 200:
                return response.text
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                raise Exception("API error: " + response.status_code)
        else:
            # request failed
            raise Exception("API error")


class MappingApi:
    """
    Base class for CUSIP/CIK/Ticker Mapping API
    Documentation: https://sec-api.io/docs/mapping-api

    cik, ticker, cusip, name, exchange, sector, industry
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = mapping_api_endpoint
        self.supported_parameters = [
            "cik",
            "ticker",
            "cusip",
            "name",
            "exchange",
            "sector",
            "industry",
        ]

    def resolve(self, parameter="", value=""):
        if not parameter.lower() in self.supported_parameters:
            raise ValueError("Parameter not supported")

        _url = (
            self.api_endpoint
            + "/"
            + parameter.lower()
            + "/"
            + value
            + "?token="
            + self.api_key
        )

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.get(_url)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                raise Exception("API error: " + response.status_code)
        else:
            # request failed
            raise Exception("API error")
