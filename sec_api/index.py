import requests
import json
import re
import time

query_api_endpoint = "https://api.sec-api.io"
full_text_search_api_endpoint = "https://api.sec-api.io/full-text-search"
filing_download_api_endpoint = "https://archive.sec-api.io"
pdf_generator_api_endpoint = "https://api.sec-api.io/filing-reader"
xbrl_api_endpoint = "https://api.sec-api.io/xbrl-to-json"
extractor_api_endpoint = "https://api.sec-api.io/extractor"
#
form_adv_endpoint = "https://api.sec-api.io/form-adv"
#
insider_api_endpoint = "https://api.sec-api.io/insider-trading"
form_144_api_endpoint = "https://api.sec-api.io/form-144"
form_13F_holdings_endpoint = "https://api.sec-api.io/form-13f/holdings"
form_13F_cover_pages_endpoint = "https://api.sec-api.io/form-13f/cover-pages"
form_nport_api_endpoint = "https://api.sec-api.io/form-nport"
form_13D_13G_endpoint = "https://api.sec-api.io/form-13d-13g"
#
form_NCEN_endpoint = "https://api.sec-api.io/form-ncen"
form_NPX_endpoint = "https://api.sec-api.io/form-npx"
#
form_S1_424B4_endpoint = "https://api.sec-api.io/form-s1-424b4"
form_d_api_endpoint = "https://api.sec-api.io/form-d"
form_C_endpoint = "https://api.sec-api.io/form-c"
reg_A_search_all_endpoint = "https://api.sec-api.io/reg-a/search"
form_1A_endpoint = "https://api.sec-api.io/reg-a/form-1a"
form_1K_endpoint = "https://api.sec-api.io/reg-a/form-1k"
form_1Z_endpoint = "https://api.sec-api.io/reg-a/form-1z"
#
form_8K_item_4_02_api_endpoint = "https://api.sec-api.io/form-8k"
form_8K_item_x_api_endpoint = "https://api.sec-api.io/form-8k"
#
exec_comp_api_endpoint = "https://api.sec-api.io/compensation"
directors_board_members_api_endpoint = (
    "https://api.sec-api.io/directors-and-board-members"
)
float_api_endpoint = "https://api.sec-api.io/float"
subsidiary_endpoint = "https://api.sec-api.io/subsidiaries"
#
sec_enforcement_actions = "https://api.sec-api.io/sec-enforcement-actions"
sec_litigations_search_endpoint = "https://api.sec-api.io/sec-litigation-releases"
sec_administrative_proceedings_endpoint = (
    "https://api.sec-api.io/sec-administrative-proceedings"
)
aaer_search_endpoint = "https://api.sec-api.io/aaers"
sro_search_endpoint = "https://api.sec-api.io/sro"
#
mapping_api_endpoint = "https://api.sec-api.io/mapping"
edgar_entities_endpoint = "https://api.sec-api.io/edgar-entities"


def handle_api_error(response):
    raise Exception("API error: {} - {}".format(response.status_code, response.text))


class QueryApi:
    """
    Base class for Query API
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = query_api_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_filings(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
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

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = full_text_search_api_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_filings(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
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

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = filing_download_api_endpoint
        self.proxies = proxies if proxies else {}

    def get_filing(self, url, return_binary=False):
        response = {}
        # remove "ix?doc=/" from URL
        filename = re.sub(r"ix\?doc=/", "", url)
        filename = re.sub(r"https://www.sec.gov/Archives/edgar/data", "", filename)
        _url = self.api_endpoint + filename + "?token=" + self.api_key

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.get(_url, proxies=self.proxies)
            if response.status_code == 200:
                return response.text if not return_binary else response.content
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)

    def get_file(self, url, return_binary=False):
        response = {}
        # remove "ix?doc=/" from URL
        filename = re.sub(r"ix\?doc=/", "", url)
        filename = re.sub(r"https://www.sec.gov/Archives/edgar/data", "", filename)
        _url = self.api_endpoint + filename + "?token=" + self.api_key

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.get(_url, proxies=self.proxies)
            if response.status_code == 200:
                return response.text if not return_binary else response.content
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class PdfGeneratorApi:
    """
    Base class for PDF Generator API
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = pdf_generator_api_endpoint
        self.proxies = proxies if proxies else {}

    def get_pdf(self, url):
        response = {}
        file_url = re.sub(r"ix\?doc=/", "", url)
        _url = (
            self.api_endpoint + "?type=pdf&url=" + file_url + "&token=" + self.api_key
        )

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.get(_url, proxies=self.proxies)
            if response.status_code == 200:
                return response.content
            elif response.status_code == 429 or response.status_code == 202:
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

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = xbrl_api_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

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
            response = requests.get(_url, proxies=self.proxies)

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

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = extractor_api_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

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
            response = requests.get(_url, proxies=self.proxies)

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

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = mapping_api_endpoint
        self.proxies = proxies if proxies else {}
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
            response = requests.get(_url, proxies=self.proxies)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class DirectorsBoardMembersApi:
    """
    Base class for Directors and Board Members API
    https://sec-api.io/docs/directors-and-board-members-data-api
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = directors_board_members_api_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
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

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = exec_comp_api_endpoint
        self.proxies = proxies if proxies else {}

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
                response = requests.get(_url, proxies=self.proxies)
            else:
                _url = self.api_endpoint + "?token=" + self.api_key
                response = requests.post(_url, json=parameter, proxies=self.proxies)

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

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = insider_api_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class Form144Api:
    """
    Base class for Form 144 API
    https://sec-api.io/docs/form-144-restricted-sales-api
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = form_144_api_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class Form13FHoldingsApi:
    """
    Base class for Form 13F Holdings API
    https://sec-api.io/docs/form-13-f-filings-institutional-holdings-api
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = form_13F_holdings_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class Form13FCoverPagesApi:
    """
    Base class for Form 13F Cover Pages API
    https://sec-api.io/docs/form-13-f-filings-institutional-holdings-api
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = form_13F_cover_pages_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
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

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = form_nport_api_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class FormCApi:
    """
    Base class for Form C API
    https://sec-api.io/docs/form-c-crowdfunding-api
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = form_C_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
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

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = form_d_api_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class RegASearchAllApi:
    """
    Base class for Regulation A Search All API
    https://sec-api.io/docs/reg-a-offering-statements-api#search-api-endpoint
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = reg_A_search_all_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class Form1AApi:
    """
    Base class for Form 1-A API
    https://sec-api.io/docs/reg-a-offering-statements-api#form-1-a-offering-statements-api
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = form_1A_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class Form1KApi:
    """
    Base class for Form 1-K API
    https://sec-api.io/docs/reg-a-offering-statements-api#form-1-k-annual-reports-api
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = form_1K_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class Form1ZApi:
    """
    Base class for Form 1-Z API
    https://sec-api.io/docs/reg-a-offering-statements-api#form-1-z-exit-reports-api
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = form_1Z_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class FormAdvApi:
    """
    Base class for Form ADV API
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint_firm = form_adv_endpoint + "/firm" + "?token=" + api_key
        self.api_endpoint_individual = (
            form_adv_endpoint + "/individual" + "?token=" + api_key
        )
        self.api_endpoint_brochures = form_adv_endpoint + "/brochures?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_firms(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint_firm, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)

    def get_request_wrapper(self, api_endpoint):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.get(api_endpoint, proxies=self.proxies)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(x + 1)
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)

    def get_direct_owners(self, crd):
        api_endpoint = (
            form_adv_endpoint
            + "/schedule-a-direct-owners/"
            + str(crd)
            + "?token="
            + self.api_key
        )
        return self.get_request_wrapper(api_endpoint)

    def get_indirect_owners(self, crd):
        api_endpoint = (
            form_adv_endpoint
            + "/schedule-b-indirect-owners/"
            + str(crd)
            + "?token="
            + self.api_key
        )
        return self.get_request_wrapper(api_endpoint)

    def get_private_funds(self, crd):
        api_endpoint = (
            form_adv_endpoint
            + "/schedule-d-7-b-1/"
            + str(crd)
            + "?token="
            + self.api_key
        )
        return self.get_request_wrapper(api_endpoint)

    def get_individuals(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint_individual, json=query, proxies=self.proxies
            )
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
        api_endpoint = (
            form_adv_endpoint + "/brochures/" + str(crd) + "?token=" + self.api_key
        )
        return self.get_request_wrapper(api_endpoint)


class FloatApi:
    """
    Base class for Float API
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = float_api_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_float(self, ticker="", cik=""):
        if len(ticker) == 0 and len(cik) == 0:
            raise Exception("Invalid input")

        response = {}

        search_term = "&ticker=" + ticker if len(ticker) else "&cik=" + cik
        url = self.api_endpoint + search_term

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.get(url, proxies=self.proxies)
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

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = form_13D_13G_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class FormNcenApi:
    """
    Base class for Form N-CEN API - Annual Reports of Registered Investment Companies
    https://sec-api.io/docs/form-ncen-api-annual-reports-investment-companies
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = form_NCEN_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class FormNPXApi:
    """
    Base class for Form N-PX Proxy Voting Records API
    https://sec-api.io/docs/form-npx-proxy-voting-records-api
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint_metadata = form_NPX_endpoint + "?token=" + api_key
        self.api_endpoint_records = (
            form_NPX_endpoint + "/<accessionNo>?token=" + api_key
        )
        self.proxies = proxies if proxies else {}

    def get_metadata(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint_metadata, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)

    def get_voting_records(self, accessionNo):
        api_endpoint = self.api_endpoint_records.replace("<accessionNo>", accessionNo)
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.get(api_endpoint, proxies=self.proxies)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class Form_S1_424B4_Api:
    """
    Base class for Form S1/424B4 API
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = form_S1_424B4_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class SubsidiaryApi:
    """
    Base class for Subsidiary API
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = subsidiary_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class SecEnforcementActionsApi:
    """
    Base class for SEC Enforcement Actions API
    https://sec-api.io/docs/sec-enforcement-actions-database-api
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_search_endpoint = sec_enforcement_actions + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_search_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class SecLitigationsApi:
    """
    Base class for SEC Litigation Releases API
    https://sec-api.io/docs/sec-litigation-releases-database-api
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_search_endpoint = sec_litigations_search_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_search_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class SecAdministrativeProceedingsApi:
    """
    Base class for SEC Administrative Proceedings API
    https://sec-api.io/docs/sec-administrative-proceedings-database-api
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_search_endpoint = (
            sec_administrative_proceedings_endpoint + "?token=" + api_key
        )
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_search_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class AaerApi:
    """
    Base class for AAER Database API
    https://sec-api.io/docs/aaer-database-api
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_search_endpoint = aaer_search_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_search_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class SroFilingsApi:
    """
    Base class for SRO Filings Database API
    https://sec-api.io/docs/sro-filings-database-api
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_search_endpoint = sro_search_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_search_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class Form_8K_Item_X_Api:
    """
    Base class for Form 8-K Item X API
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = form_8K_item_x_api_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class Item_4_02_Api:
    """
    Base class for Form 8-K Item 4.02 API
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = form_8K_item_4_02_api_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)


class EdgarEntitiesApi:
    """
    Base class for EDGAR Entities Database API
    https://sec-api.io/docs/edgar-entities-database-api
    """

    def __init__(self, api_key, proxies=None):
        self.api_key = api_key
        self.api_endpoint = edgar_entities_endpoint + "?token=" + api_key
        self.proxies = proxies if proxies else {}

    def get_data(self, query):
        response = {}

        # use backoff strategy to handle "too many requests" error.
        for x in range(3):
            response = requests.post(
                self.api_endpoint, json=query, proxies=self.proxies
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # wait 500 * (x + 1) milliseconds and try again
                time.sleep(0.5 * (x + 1))
            else:
                handle_api_error(response)
        else:
            handle_api_error(response)
