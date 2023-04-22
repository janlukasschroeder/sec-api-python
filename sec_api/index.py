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
exec_comp_api_endpoint = "https://api.sec-api.io/compensation"
insider_api_endpoint = "https://api.sec-api.io/insider-trading"
form_nport_api_endpoint = "https://api.sec-api.io/form-nport"
form_d_api_endpoint = "https://api.sec-api.io/form-d"
form_adv_endpoint = "https://api.sec-api.io/form-adv"
form_13D_13G_endpoint = "https://api.sec-api.io/form-13d-13g"
float_api_endpoint = "https://api.sec-api.io/float"


def handle_api_error(response):
    raise Exception("API error: {} - {}".format(response.status_code, response.text))


class QueryApi:
    """
    Base class for Query API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = query_api_endpoint + "?token=" + api_key

    def get_filings(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(self.api_endpoint, json=query)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class FullTextSearchApi:
    """
    Base class for Full-Text Search API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = full_text_search_api_endpoint + "?token=" + api_key

    def get_filings(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(self.api_endpoint, json=query)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class RenderApi:
    """
    Base class for Render API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = render_api_endpoint

    def get_filing(self, url, as_pdf=False):
        response = {}
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
                handle_api_error(response)
        else:
            handle_api_error(response)


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
        response = {}

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
                handle_api_error(response)
        else:
            handle_api_error(response)


class ExtractorApi:
    """
    Base class for 10-K/10-Q/8-K item/section extractor API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = extractor_api_endpoint + "?token=" + api_key

    def get_section(self, filing_url="", section="1A", return_type="text"):
        if len(filing_url) == 0:
            raise ValueError("filing_url must be present")

        response = {}
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
        for x in range(5):
            response = requests.get(_url)

            if response.status_code == 200:
                return response.text
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


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

        response = {}
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
                handle_api_error(response)
        else:
            handle_api_error(response)


class ExecCompApi:
    """
    Base class of Executive Compensation Data API
    Documentation: https://sec-api.io/docs/executive-compensation-api
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = exec_comp_api_endpoint

    def get_data(self, parameter=""):
        if isinstance(parameter, str):
            http_method = "GET"
        elif isinstance(parameter, dict):
            http_method = "POST"
        else:
            raise Exception("Invalid parameter")

        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            if http_method == "GET":
                _url = (
                    self.api_endpoint
                    + "/"
                    + parameter.upper()
                    + "?token="
                    + self.api_key
                )
                response = requests.get(_url)
            else:
                _url = self.api_endpoint + "?token=" + self.api_key
                response = requests.post(_url, json=parameter)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class InsiderTradingApi:
    """
    Base class for Insider Trading Data API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = insider_api_endpoint + "?token=" + api_key

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(self.api_endpoint, json=query)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class FormNportApi:
    """
    Base class for Form NPORT API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = form_nport_api_endpoint + "?token=" + api_key

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(self.api_endpoint, json=query)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class FormDApi:
    """
    Base class for Form D API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = form_d_api_endpoint + "?token=" + api_key

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(self.api_endpoint, json=query)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class FormAdvApi:
    """
    Base class for Form ADV API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint_firm = form_adv_endpoint + "/firm" + "?token=" + api_key
        self.api_endpoint_individual = (
            form_adv_endpoint + "/individual" + "?token=" + api_key
        )
        self.api_endpoint_brochures = form_adv_endpoint + "/brochures?token=" + api_key

    def get_firms(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(self.api_endpoint_firm, json=query)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)

    def get_individuals(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(self.api_endpoint_individual, json=query)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)

    def get_brochures(self, crd):
        endpoint = (
            form_adv_endpoint + "/brochures/" + str(crd) + "?token=" + self.api_key
        )
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class FloatApi:
    """
    Base class for Float API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = float_api_endpoint + "?token=" + api_key

    def get_float(self, ticker="", cik=""):
        if len(ticker) == 0 and len(cik) == 0:
            raise Exception("Invalid input")

        response = {}

        search_term = "&ticker=" + ticker if len(ticker) else "&cik=" + cik
        url = self.api_endpoint + search_term

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class Form13DGApi:
    """
    Base class for Form 13D/13G API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = form_13D_13G_endpoint + "?token=" + api_key

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(self.api_endpoint, json=query)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)
