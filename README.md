# SEC API - Access SEC and EDGAR Data with Python

[![Downloads](https://pepy.tech/badge/sec-api)](https://pepy.tech/project/sec-api) [![Documentation](https://img.shields.io/badge/Documentation-sec--api.io-blue)](https://sec-api.io/docs)

**sec-api** is a Python package for searching and accessing the entire SEC EDGAR filings corpus, providing access to petabytes of regulatory data from public and private companies, insiders (directors, board members, etc.), funds (ETFs, hedge funds, etc.), financial advisors, business development companies, and more. It includes:

**EDGAR Filing Search & Download APIs**

- [SEC Filing Search and Full-Text Search API](#sec-edgar-filings-query-api)
- [Real-Time Filing Stream API](#sec-edgar-filings-real-time-stream-api)
- [Download API - Download any SEC filing, exhibit and attached file](#filing--exhibit-download-api)
- [PDF Generator API - Download SEC filings and exhibits as PDF](#pdf-generator-api)

**Converter & Extractor APIs**

- [XBRL-to-JSON Converter API + Financial Statements](#xbrl-to-json-converter-api)
- [10-K/10-Q/8-K Section Extraction API](#10-k10-q8-k-section-extractor-api)

**Investment Advisers**

- [Form ADV API - Investment Advisors (Firm & Indvl. Advisors, Brochures, Schedules)](#form-adv-api)

**Ownership Data APIs**

- [Form 3/4/5 API - Insider Trading Disclosures](#insider-trading-data-api)
- [Form 144 API - Restricted Stock Sales by Insiders](#form-144-api)
- [Form 13F API - Institutional Investment Manager Holdings & Cover Pages](#form-13f-institutional-holdings-database)
- [Form 13D/13G API - Activist and Passive Investor Holdings](#form-13d-13g-api)
- [Form N-PORT API - Mutual Funds, ETFs and Closed-End Fund Holdings](#form-n-port-api)

**Proxy Voting Records**

- [Form N-PX Proxy Voting Records API](#form-n-px-proxy-voting-records-api)

**Security Offerings APIs**

- [Form S-1/424B4 API - Registration Statements and Prospectuses (IPOs, Debt/Warrants/... Offerings)](#form-s-1424b4-api)
- [Form C API - Crowdfunding Offerings & Campaigns](#form-c-api---crowdfunding-campaigns)
- [Form D API - Private Security Offerings](#form-d-api)
- [Regulation A APIs - Offering Statements by Small Companies (Form 1-A, Form 1-K, Form 1-Z)](#regulation-a-apis)

**Structured Material Event Data from Form 8-K**

- [Auditor and Accountant Changes (Item 4.01)](#auditor-and-accountant-changes-item-401)
- [Financial Restatements & Non-Reliance on Prior Financial Results (Item 4.02)](#financial-restatements--non-reliance-on-prior-financial-results-item-402)
- [Changes of Directors, Board Members and Compensation Plans (Item 5.02)](#changes-of-directors-executives-board-members-and-compensation-plans-item-502)

**Public Company Data**

- [Directors & Board Members API](#directors--board-members-data-api)
- [Executive Compensation Data API](#executive-compensation-data-api)
- [Outstanding Shares & Public Float](#outstanding-shares--public-float-api)
- [Company Subsidiary API](#subsidiary-api)

**Enforcement Actions, Proceedings, AAERs & SRO Filings**

- [SEC Enforcement Actions](#sec-enforcement-actions-database-api)
- [SEC Litigation Releases](#sec-litigation-releases-database-api)
- [SEC Administrative Proceedings](#sec-administrative-proceedings-database-api)
- [AAER Database API - Accounting and Auditing Enforcement Releases](#aaer-database-api)
- [SRO Filings Database API](#sro-filings-database-api)

**Other APIs**

- [CUSIP/CIK/Ticker Mapping API](#cusipcikticker-mapping-api)
- [EDGAR Entities Database API](#edgar-entities-database)

## Data Coverage

- Access to over 18 million SEC EDGAR filings from 1993 to the present
- Supports all 150+ filing types, including 10-Q, 10-K, Form 4, 8-K, 13-F, S-1, 424B4, and many others. [See the full list of supported form types here.](https://sec-api.io/list-of-sec-filing-types)
- Real-time access to newly published filings.
- Includes XBRL-to-JSON converter and parser APIs for extracting standardized financial statements from any 10-K or 10-Q filing.
- 13F Holdings API provided, allowing real-time monitoring of institutional ownership.
- Every filing is linked to its corresponding CIK and ticker.
- All filings available in JSON format — no need for XBRL/XML parsing.

## Overview

- The Query API gives access to all over 18 million SEC EDGAR filings of over 8,000 publicly listed companies, ETFs, hedge funds, mutual funds, and investors dating back to 1993.
- Connect to the real-time stream API to receive new filings as soon as they are published on SEC EDGAR
- The Full-Text Search API allows you to search the full text of all filings submitted since 2001. The full text of a filing includes all data in the filing itself as well as all attachments (such as exhibits) to the filing.
- Free API key available on [sec-api.io](https://sec-api.io)

See the official documentation for more: [sec-api.io/docs](https://sec-api.io/docs)

## Installation

```bash
pip install sec-api
```

Get your free API key on [sec-api.io](https://sec-api.io) and replace `YOUR_API_KEY` with it.

## SEC EDGAR Filings Query API

The Query API allows you to search and filter all 18 million filings and exhibits published on SEC EDGAR using a large set of search parameters. The database behind the Query API includes all EDGAR filing form types published since 1993 and over 800,000 EDGAR filer entities, with new filings being indexed and searchable as soon as they are published on SEC EDGAR.

You can search filings by ticker, CIK, form type, filing date, SIC code, period of report, series and class IDs, items of 8-K and other filings, and many more. The API returns all filing metadata in a [standardized JSON format](https://sec-api.io/docs/query-api#response-format).

Examples are provided below, in the [official documentation](https://sec-api.io/docs/query-api), and in our [sandbox](https://sec-api.io/sandbox).

### Examples

The following example retrieves all 10-Q filings filed by TSLA in 2020.

```python
from sec_api import QueryApi

queryApi = QueryApi(api_key="YOUR_API_KEY")

query = {
  "query": "ticker:TSLA AND filedAt:[2020-01-01 TO 2020-12-31] AND formType:\"10-Q\"",
  "from": "0",
  "size": "10",
  "sort": [{ "filedAt": { "order": "desc" } }]
}

filings = queryApi.get_filings(query)

print(filings)
```

Find the most recently reported Form 8-K filings that include Item 9.01 "Financial Statements and Exhibits".

```python
query = {
  "query": "formType:\"8-K\" AND items:\"9.01\"",
  "from": "0",
  "size": "10",
  "sort": [{ "filedAt": { "order": "desc" } }]
}

filings = queryApi.get_filings(query)
```

> See the documentation for more details: https://sec-api.io/docs/query-api

## Full-Text Search API

Full-text search allows you to search the full text of all EDGAR filings submitted since 2001. The full text of a filing includes all data in the filing itself as well as all attachments (such as exhibits) to the filing.

---

The example below returns all 8-K and 10-Q filings and their exhibits, filed between 01-01-2021 and 14-06-2021, that include the exact phrase "LPCN 1154".

```python
from sec_api import FullTextSearchApi

fullTextSearchApi = FullTextSearchApi(api_key="YOUR_API_KEY")

query = {
  "query": '"LPCN 1154"',
  "formTypes": ['8-K', '10-Q'],
  "startDate": '2021-01-01',
  "endDate": '2021-06-14',
}

filings = fullTextSearchApi.get_filings(query)

print(filings)
```

> See the documentation for more details: https://sec-api.io/docs/full-text-search-api

## Filing & Exhibit Download API

Download any SEC EDGAR filing, exhibit and attached file in its original format (HTML, XML, JPEG, Excel, text, PDF, etc.). The API supports downloading all EDGAR form types, including 10-K, 10-Q, 8-K, 13-F, S-1, 424B4, and many others published since 1993 and provides access to over 18 million filings and over 100 million exhibits and filing attachments. Download up to 40 files per second.

```python
from sec_api import RenderApi

renderApi = RenderApi(api_key="YOUR_API_KEY")

# example URLs: SEC filings, exhibits, images, Excel sheets, PDFs
url_8k_html       = "https://www.sec.gov/Archives/edgar/data/1045810/000104581023000014/nvda-20230222.htm"
url_8k_txt        = "https://www.sec.gov/Archives/edgar/data/1045810/000104581023000014/0001045810-23-000014.txt"
url_exhibit99     = "https://www.sec.gov/Archives/edgar/data/1045810/000104581023000014/q4fy23pr.htm"
url_xbrl_instance = "https://www.sec.gov/Archives/edgar/data/1045810/000104581023000014/nvda-20230222_htm.xml"
url_excel_file    = "https://www.sec.gov/Archives/edgar/data/1045810/000104581023000014/Financial_Report.xlsx"
url_pdf_file      = "https://www.sec.gov/Archives/edgar/data/1798925/999999999724004095/filename1.pdf"
url_image_file    = "https://www.sec.gov/Archives/edgar/data/1424404/000106299324017776/form10kxz001.jpg"

filing_8k_html = renderApi.get_file(url_8k_html)
filing_8k_txt  = renderApi.get_file(url_8k_txt)
exhibit99      = renderApi.get_file(url_exhibit99)
xbrl_instance  = renderApi.get_file(url_xbrl_instance)

# use .get_file() and set return_binary=True
# to get non-text files such as images, PDFs, etc.
excel_file     = renderApi.get_file(url_excel_file, return_binary=True)
pdf_file       = renderApi.get_file(url_pdf_file, return_binary=True)
image_file     = renderApi.get_file(url_image_file, return_binary=True)

# save files to disk
with open("filing_8k_html.htm", "wb") as f:
    f.write(filing_8k_html.encode("utf-8"))
with open("pdf_file.pdf", "wb") as f:
    f.write(pdf_file)
with open("image.jpg", "wb") as f:
    f.write(image_file)
```

> See the documentation for more details: https://sec-api.io/docs/sec-filings-render-api

## PDF Generator API

SEC filings, including Forms 10-K, 10-Q, 8-K, and others, are typically published in HTML, XML, or text formats. The PDF Generator API enables the conversion of any SEC filing or exhibit into a PDF file, preserving all original formatting, tables, images, and other elements from the filing.

```python
from sec_api import PdfGeneratorApi

pdfGeneratorApi = PdfGeneratorApi("YOUR_API_KEY")

# examples: 10-K filing, Form 8-K exhibit
url_10k_filing = "https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/aapl-20200926.htm"
url_8k_exhibit_url = "https://www.sec.gov/ix?doc=/Archives/edgar/data/1320695/000132069520000148/ths12-31x201910krecast.htm"

# get PDFs
pdf_10k_filing = pdfGeneratorApi.get_pdf(url_10k_filing)
pdf_8k_exhibit = pdfGeneratorApi.get_pdf(url_8k_exhibit_url)

# save PDFs to disk
with open("pdf_10k_filing.pdf", "wb") as f:
    f.write(pdf_10k_filing)
with open("pdf_8k_exhibit.pdf", "wb") as f:
    f.write(pdf_8k_exhibit)
```

> See the documentation for more details: https://sec-api.io/docs/sec-filings-render-api

## SEC EDGAR Filings Real-Time Stream API

The Stream API provides a live stream (aka feed) of newly published filings on SEC EDGAR via WebSockets. A new filing is sent to your connected client as soon as it is published.

---

Install the `websockets` client:

```bash
pip install websockets
```

Run the example script below. Get your free API key on [sec-api.io](https://sec-api.io) and replace `YOUR_API_KEY` with it.

```python
import asyncio
import websockets
import json

API_KEY = "YOUR_API_KEY" # Replace this with your actual API key
SERVER_URL = "wss://stream.sec-api.io"
WS_ENDPOINT = SERVER_URL + "?apiKey=" + API_KEY

async def websocket_client():
    try:
        async with websockets.connect(WS_ENDPOINT) as websocket:
            print("✅ Connected to:", SERVER_URL)

            while True:
                message = await websocket.recv()
                filings = json.loads(message)
                for f in filings:
                    print(f["accessionNo"], f["formType"], f["filedAt"], f["cik"])

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


asyncio.run(websocket_client())
```

> See the documentation for more details: https://sec-api.io/docs/stream-api

## XBRL-To-JSON Converter API

Parse and standardize any XBRL and convert it to JSON or pandas dataframes. Extract financial statements and metadata from 10-K, 10-Q and any other SEC filing supporting XBRL.

The entire US GAAP taxonomy is fully supported. All XBRL items are fully converted into JSON, including `us-gaap`, `dei` and custom items. XBRL facts are automatically mapped to their respective context including period instants and date ranges.

All financial statements are accessible and standardized:

- StatementsOfIncome
- StatementsOfIncomeParenthetical
- StatementsOfComprehensiveIncome
- StatementsOfComprehensiveIncomeParenthetical
- BalanceSheets
- BalanceSheetsParenthetical
- StatementsOfCashFlows
- StatementsOfCashFlowsParenthetical
- StatementsOfShareholdersEquity
- StatementsOfShareholdersEquityParenthetical

Variants such as `ConsolidatedStatementsofOperations` or `ConsolidatedStatementsOfLossIncome` are automatically standardized to their root name, e.g. `StatementsOfIncome`.

### Income Statement - Example Item

```json
{
  "StatementsOfIncome": {
    "RevenueFromContractWithCustomerExcludingAssessedTax": [
      {
        "decimals": "-6",
        "unitRef": "usd",
        "period": {
          "startDate": "2019-09-29",
          "endDate": "2020-09-26"
        },
        "value": "274515000000"
      },
      {
        "decimals": "-6",
        "unitRef": "usd",
        "period": {
          "startDate": "2018-09-30",
          "endDate": "2019-09-28"
        },
        "value": "260174000000"
      }
    ]
  }
}
```

### Usage

There are 3 ways to convert XBRL to JSON:

- `htm_url`: Provide the URL of the filing ending with `.htm`.
  Example URL: https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231.htm
- `xbrl_url`: Provide the URL of the XBRL file ending with `.xml`. The XBRL file URL can be found in the `dataFiles` array returned by our query API. The array item has the description `EXTRACTED XBRL INSTANCE DOCUMENT` or similar.
  Example URL: https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231_htm.xml
- `accession_no`: Provide the accession number of the filing, e.g. `0001564590-21-004599`

```python
from sec_api import XbrlApi

xbrlApi = XbrlApi("YOUR_API_KEY")

# 10-K HTM File URL example
xbrl_json = xbrlApi.xbrl_to_json(
    htm_url="https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/aapl-20200926.htm"
)

# access income statement, balance sheet and cash flow statement
print(xbrl_json["StatementsOfIncome"])
print(xbrl_json["BalanceSheets"])
print(xbrl_json["StatementsOfCashFlows"])

# 10-K XBRL File URL example
xbrl_json = xbrlApi.xbrl_to_json(
    xbrl_url="https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231_htm.xml"
)

# 10-K accession number example
xbrl_json = xbrlApi.xbrl_to_json(accession_no="0001564590-21-004599")
```

### Example Response

Note: response is shortened.

```json
{
  "CoverPage": {
    "DocumentPeriodEndDate": "2020-09-26",
    "EntityRegistrantName": "Apple Inc.",
    "EntityIncorporationStateCountryCode": "CA",
    "EntityTaxIdentificationNumber": "94-2404110",
    "EntityAddressAddressLine1": "One Apple Park Way",
    "EntityAddressCityOrTown": "Cupertino",
    "EntityAddressStateOrProvince": "CA",
    "EntityAddressPostalZipCode": "95014",
    "CityAreaCode": "408",
    "LocalPhoneNumber": "996-1010",
    "TradingSymbol": "AAPL",
    "EntityPublicFloat": {
      "decimals": "-6",
      "unitRef": "usd",
      "period": {
        "instant": "2020-03-27"
      },
      "value": "1070633000000"
    },
    "EntityCommonStockSharesOutstanding": {
      "decimals": "-3",
      "unitRef": "shares",
      "period": {
        "instant": "2020-10-16"
      },
      "value": "17001802000"
    },
    "DocumentFiscalPeriodFocus": "FY",
    "CurrentFiscalYearEndDate": "--09-26"
  },
  "StatementsOfIncome": {
    "RevenueFromContractWithCustomerExcludingAssessedTax": [
      {
        "decimals": "-6",
        "unitRef": "usd",
        "period": {
          "startDate": "2019-09-29",
          "endDate": "2020-09-26"
        },
        "segment": {
          "dimension": "srt:ProductOrServiceAxis",
          "value": "us-gaap:ProductMember"
        },
        "value": "220747000000"
      },
      {
        "decimals": "-6",
        "unitRef": "usd",
        "period": {
          "startDate": "2018-09-30",
          "endDate": "2019-09-28"
        },
        "segment": {
          "dimension": "srt:ProductOrServiceAxis",
          "value": "us-gaap:ProductMember"
        },
        "value": "213883000000"
      }
    ]
  },
  "BalanceSheets": {
    "CashAndCashEquivalentsAtCarryingValue": [
      {
        "decimals": "-6",
        "unitRef": "usd",
        "period": {
          "instant": "2020-09-26"
        },
        "value": "38016000000"
      },
      {
        "decimals": "-6",
        "unitRef": "usd",
        "period": {
          "instant": "2019-09-28"
        },
        "value": "48844000000"
      },
      {
        "decimals": "-6",
        "unitRef": "usd",
        "period": {
          "instant": "2020-09-26"
        },
        "segment": {
          "dimension": "us-gaap:FinancialInstrumentAxis",
          "value": "us-gaap:CashMember"
        },
        "value": "17773000000"
      }
    ]
  }
}
```

> See the documentation for more details: https://sec-api.io/docs/xbrl-to-json-converter-api

## 10-K/10-Q/8-K Section Extractor API

The Extractor API returns individual sections from 10-Q, 10-K and 8-K filings. The extracted section is cleaned and standardized - in raw text or in standardized HTML. You can programmatically extract one or multiple sections from any 10-Q, 10-K and 8-K filing.

**All 10-K sections can be extracted:**

- 1 - Business
- 1A - Risk Factors
- 1B - Unresolved Staff Comments
- 1C - Cybersecurity (introduced in 2023)
- 2 - Properties
- 3 - Legal Proceedings
- 4 - Mine Safety Disclosures
- 5 - Market for Registrant’s Common Equity, Related Stockholder Matters and Issuer Purchases of Equity Securities
- 6 - Selected Financial Data (prior to February 2021)
- 7 - Management’s Discussion and Analysis of Financial Condition and Results of Operations
- 7A - Quantitative and Qualitative Disclosures about Market Risk
- 8 - Financial Statements and Supplementary Data
- 9 - Changes in and Disagreements with Accountants on Accounting and Financial Disclosure
- 9A - Controls and Procedures
- 9B - Other Information
- 10 - Directors, Executive Officers and Corporate Governance
- 11 - Executive Compensation
- 12 - Security Ownership of Certain Beneficial Owners and Management and Related Stockholder Matters
- 13 - Certain Relationships and Related Transactions, and Director Independence
- 14 - Principal Accountant Fees and Services

**All 10-Q sections can be extracted:**

Part 1:

- 1 - Financial Statements
- 2 - Management’s Discussion and Analysis of Financial Condition and Results of Operations
- 3 - Quantitative and Qualitative Disclosures About Market Risk
- 4 - Controls and Procedures

Part 2:

- 1 - Legal Proceedings
- 1A - Risk Factors
- 2 -Unregistered Sales of Equity Securities and Use of Proceeds
- 3 - Defaults Upon Senior Securities
- 4 - Mine Safety Disclosures
- 5 - Other Information
- 6 - Exhibits

**All 8-K sections can be extracted:**

- 1.01: Entry into a Material Definitive Agreement
- 1.02: Termination of a Material Definitive Agreement
- 1.03: Bankruptcy or Receivership
- 1.04: Mine Safety - Reporting of Shutdowns and Patterns of Violations
- 1.05: Material Cybersecurity Incidents (introduced in 2023)
- 2.01: Completion of Acquisition or Disposition of Assets
- 2.02: Results of Operations and Financial Condition
- 2.03: Creation of a Direct Financial Obligation or an Obligation under an Off-Balance Sheet Arrangement of a Registrant
- 2.04: Triggering Events That Accelerate or Increase a Direct Financial Obligation or an Obligation under an Off-Balance Sheet Arrangement
- 2.05: Cost Associated with Exit or Disposal Activities
- 2.06: Material Impairments
- 3.01: Notice of Delisting or Failure to Satisfy a Continued Listing Rule or Standard; Transfer of Listing
- 3.02: Unregistered Sales of Equity Securities
- 3.03: Material Modifications to Rights of Security Holders
- 4.01: Changes in Registrant's Certifying Accountant
- 4.02: Non-Reliance on Previously Issued Financial Statements or a Related Audit Report or Completed Interim Review
- 5.01: Changes in Control of Registrant
- 5.02: Departure of Directors or Certain Officers; Election of Directors; Appointment of Certain Officers: Compensatory Arrangements of Certain Officers
- 5.03: Amendments to Articles of Incorporation or Bylaws; Change in Fiscal Year
- 5.04: Temporary Suspension of Trading Under Registrant's Employee Benefit Plans
- 5.05: Amendments to the Registrant's Code of Ethics, or Waiver of a Provision of the Code of Ethics
- 5.06: Change in Shell Company Status
- 5.07: Submission of Matters to a Vote of Security Holders
- 5.08: Shareholder Nominations Pursuant to Exchange Act Rule 14a-11
- 6.01: ABS Informational and Computational Material
- 6.02: Change of Servicer or Trustee
- 6.03: Change in Credit Enhancement or Other External Support
- 6.04: Failure to Make a Required Distribution
- 6.05: Securities Act Updating Disclosure
- 6.06: Static Pool
- 6.10: Alternative Filings of Asset-Backed Issuers
- 7.01: Regulation FD Disclosure
- 8.01: Other Events
- 9.01: Financial Statements and Exhibits
- Signature

### Usage

```python
from sec_api import ExtractorApi

extractorApi = ExtractorApi("YOUR_API_KEY")

#
# 10-K example
#
# Tesla 10-K filing
filing_url_10k = "https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231.htm"

# get the standardized and cleaned text of section 1A "Risk Factors"
section_text = extractorApi.get_section(filing_url_10k, "1A", "text")

# get the original HTML of section 7 "Management’s Discussion and Analysis of Financial Condition and Results of Operations"
section_html = extractorApi.get_section(filing_url_10k, "7", "html")

#
# 10-Q example
#
# Tesla 10-Q filing
filing_url_10q = "https://www.sec.gov/Archives/edgar/data/1318605/000095017022006034/tsla-20220331.htm"

# extract section 1A "Risk Factors" in part 2 as cleaned text
extracted_section_10q = extractorApi.get_section(filing_url_10q, "part2item1a", "text")

#
# 8-K example
#
filing_url_8k = "https://www.sec.gov/Archives/edgar/data/66600/000149315222016468/form8-k.htm"

# extract section 1.01 "Entry into Material Definitive Agreement" as cleaned text
extracted_section_8k = extractorApi.get_section(filing_url_8k, "1-1", "text")
```

> See the documentation for more details: https://sec-api.io/docs/sec-filings-item-extraction-api

## Form ADV API

Search the entire Form ADV filing database and find all ADV filings filed by firm advisers (SEC and state registered), individual advisers and firm brochures published in part 2 of ADV filings. The database comprises 41,000 ADV filings filed by advisory firms and 380,000 individual advisers and is updated daily. Search and find ADV filings by any filing property, such as CRD, assets under management, type of adviser (e.g. broker dealer) and more. Direct owners from Schedule A, indirect owners from Schedule B as well as private funds from Schedule D are easily accessible.

```python
from sec_api import FormAdvApi

formAdvApi = FormAdvApi("YOUR_API_KEY")

response = formAdvApi.get_firms(
    {
        "query": "Info.FirmCrdNb:361",
        "from": "0",
        "size": "10",
        "sort": [{"Info.FirmCrdNb": {"order": "desc"}}],
    }
)
print(response["filings"])

direct_owners = formAdvApi.get_direct_owners(crd="793")
print(direct_owners)

indirect_owners = formAdvApi.get_indirect_owners(crd="326262")
print(indirect_owners)

private_funds = formAdvApi.get_private_funds(crd="793")
print(private_funds)

response = formAdvApi.get_individuals(
    {
        "query": "CrntEmps.CrntEmp.orgPK:149777",
        "from": "0",
        "size": "10",
        "sort": [{"id": {"order": "desc"}}],
    }
)
print(response["filings"])

response = formAdvApi.get_brochures(149777)
print(response["brochures"])
```

> See the documentation for more details: https://sec-api.io/docs/investment-adviser-and-adv-api

## Insider Trading Data API

The Insider Trading Data API allows you to search and list all insider buy and sell transactions of all publicly listed companies on US stock exchanges. Insider activities of company directors, officers, 10% owners and other executives are fully searchable. The insider trading database includes information about the CIK and name of the insider, her/his relationship to the company, the number of shares and securities purchased or sold, the purchase or selling price, the date of the transaction, the amount of securities held before and after the transaction occured, any footnotes such as the effect of Rule 10b-18 or 10b5-1 stock purchase plans and more. The full list of all data points is available below.

```python
from sec_api import InsiderTradingApi

insiderTradingApi = InsiderTradingApi("YOUR_API_KEY")

insider_trades = insiderTradingApi.get_data({
  "query": "issuer.tradingSymbol:TSLA"
})

print(insider_trades["transactions"])
```

> See the documentation for more details: https://sec-api.io/docs/insider-ownership-trading-api

### Response Example

```json
[
  {
    "accessionNo": "0000899243-22-028189",
    "filedAt": "2022-08-09T21:23:00-04:00",
    "documentType": "4",
    "periodOfReport": "2022-08-09",
    "issuer": {
      "cik": "1318605",
      "name": "Tesla, Inc.",
      "tradingSymbol": "TSLA"
    },
    "reportingOwner": {
      "cik": "1494730",
      "name": "Musk Elon",
      "address": {
        "street1": "C/O TESLA, INC.",
        "street2": "1 TESLA ROAD",
        "city": "AUSTIN",
        "state": "TX",
        "zipCode": "78725"
      },
      "relationship": {
        "isDirector": true,
        "isOfficer": true,
        "officerTitle": "CEO",
        "isTenPercentOwner": true,
        "isOther": false
      }
    },
    "nonDerivativeTable": {
      "transactions": [
        {
          "securityTitle": "Common Stock",
          "transactionDate": "2022-08-09",
          "coding": {
            "formType": "4",
            "code": "S",
            "equitySwapInvolved": false
          },
          "amounts": {
            "shares": 435,
            "pricePerShare": 872.469,
            "pricePerShareFootnoteId": ["F1"],
            "acquiredDisposedCode": "D"
          }
        }
      ]
      // and many more
    }
  }
]
```

## Form 144 API

The Form 144 API allows you to search and access all Form 144 filings from 2022 to present. Form 144 filings are filed with the SEC by corporate insiders who intend to sell restricted securities, such as vested stocks. The database includes information about the CIK and name of the insider, the issuer name and trading symbol, number of shares intended to be sold, the date of the transaction, the total value of the transaction, and more.

```python
from sec_api import Form144Api

form144Api = Form144Api("YOUR_API_KEY")

search_params = {
    "query": "entities.ticker:TSLA",
    "from": "0",
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = form144Api.get_data(search_params)

print(response["data"])
```

> See the documentation for more details: https://sec-api.io/docs/form-144-restricted-sales-api

## Form 13F Institutional Holdings Database

Access Form 13F holdings in structured JSON format, including information on current and historical portfolio holdings of SEC-registered funds and investment managers, including issuer name, title of the securities class, CUSIP, CIK and ticker of the holding, value of the position in dollar, the number of shares held, investment discretion, voting authority, and more.

```python
from sec_api import Form13FHoldingsApi

form13FHoldingsApi = Form13FHoldingsApi(api_key="YOUR_API_KEY")

search_params = {
  "query": "cik:1350694 AND periodOfReport:2024-03-31",
  "from": "0",
  "size": "10",
  "sort": [{ "filedAt": { "order": "desc" } }]
}

response = form13FHoldingsApi.get_data(search_params)
holdings = response["data"]

print(holdings)
```

> See the documentation for more details: https://sec-api.io/docs/form-13-f-filings-institutional-holdings-api

## Form 13F Cover Pages API

Search and access cover pages of Form 13F filings in standardized JSON format. Cover pages include details about the investment manager and fund, such as CIK, SEC file and CRD number, name, address, report type, other managers, and more.

```python
from sec_api import Form13FCoverPagesApi

form13FCoverPagesApi = Form13FCoverPagesApi(api_key="YOUR_API_KEY")

search_params = {
    "query": "cik:1698218 AND periodOfReport:[2023-01-1 TO 2024-12-31]",
    "from": "0",
    "size": "10",
    "sort": [{ "filedAt": { "order": "desc" }}]
}

response = form13FCoverPagesApi.get_data(query)
cover_pages = response["data"]

print(cover_pages)
```

> See the documentation for more details: https://sec-api.io/docs/form-13-f-filings-institutional-holdings-api

## Form 13D/13G API

The API allows you to easily search and access all SEC Form 13D and Form 13G filings in a standardized JSON format. You can search the database by any form field, such as the CUSIP of the acquired security, name of the security owner, or the aggregate amount owned in percetnage of total shares outstanding.

```python
from sec_api import Form13DGApi

form13DGApi = Form13DGApi("YOUR_API_KEY")

# find the 50 most recently filed 13D/G filings disclosing 10% of more ownership of any Point72 company.
query = {
    "query": "owners.name:Point72 AND owners.amountAsPercent:[10 TO *]",
    "from": "0",
    "size": "50",
    "sort": [ { "filedAt": { "order": "desc"  } } ]
}

response = form13DGApi.get_data(query)

print(response["filings"])
```

> See the documentation for more details: https://sec-api.io/docs/form-13d-13g-search-api

### Response Example

```json
{
  "total": {
    "value": 8,
    "relation": "eq"
  },
  "filings": [
    {
      "id": "bbb1ef1892bfc12a2e398c903871e3ae",
      "accessionNo": "0000902664-22-005029",
      "formType": "SC 13D",
      "filedAt": "2022-12-05T16:00:20-05:00",
      "filers": [
        {
          "cik": "1813658",
          "name": "Tempo Automation Holdings, Inc. (Subject)"
        },
        {
          "cik": "1954961",
          "name": "Point72 Private Investments, LLC (Filed by)"
        }
      ],
      "nameOfIssuer": "Tempo Automation Holdings, Inc.",
      "titleOfSecurities": "Common Stock, par value $0.0001 per share",
      "cusip": ["88024M108"],
      "eventDate": "2022-11-22",
      "schedule13GFiledPreviously": false,
      "owners": [
        {
          "name": "Point72 Private Investments, LLC",
          "memberOfGroup": {
            "a": false,
            "b": false
          },
          "sourceOfFunds": ["OO"],
          "legalProceedingsDisclosureRequired": false,
          "place": "Delaware",
          "soleVotingPower": 0,
          "sharedVotingPower": 5351000,
          "soleDispositivePower": 0,
          "sharedDispositivePower": 5351000,
          "aggregateAmountOwned": 5351000,
          "amountExcludesCertainShares": false,
          "amountAsPercent": 20.3,
          "typeOfReportingPerson": ["OO"]
        }
      ]
    }
  ]
}
```

## Form N-PORT API

Access and find standardized N-PORT SEC filings.

```python
from sec_api import FormNportApi

nportApi = FormNportApi("YOUR_API_KEY")

search_params =  {
    "query": "fundInfo.totAssets:[100000000 TO *]",
    "from": "0",
    "size": "10",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = nportApi.get_data(search_params)

print(response["filings"])
```

> See the documentation for more details: https://sec-api.io/docs/n-port-data-api

## Form N-PX Proxy Voting Records API

The Form N-PX API consists of two APIs: the N-PX Search API and the Voting Records API. The N-PX Search API enables filtering all N-PX filings published on the SEC EDGAR database since 2024. The API accepts search queries as JSON formatted payload and returns the matching N-PX filings in JSON format. The Voting Records API allows downloading the proxy voting records in structured JSON format for a specific filing by providing the filing's accession number.

```python
from sec_api import FormNPXApi

formNpxApi = FormNPXApi("YOUR_API_KEY")

search_params = {
    "query": "cik:884546",
    "from": "0",
    "size": "1",
    "sort": [{"filedAt": {"order": "desc"}}],
}

# get N-PX filing metadata: registrant type, investment company type,
# series and class IDs, report type, period of report, and more
response = formNpxApi.get_metadata(search_params)
npx_filing_metadata = response["data"]

print(npx_filing_metadata)

# get proxy voting records: issuer name, CUSIP, meeting date, vote description,
# vote categories, shares voted, how voted, management recommendation, and more
accessionNo = npx_filing_metadata[0]["accessionNo"]
response = formNpxApi.get_voting_records(accessionNo)
voting_records = response["proxyVotingRecords"]

print(voting_records[0])
```

> See the documentation for more details: https://sec-api.io/docs/form-npx-proxy-voting-records-api

## Form S-1/424B4 API

Access and find structured and standardized data extracted from S-1, F-1, and S-11 registration statements as well as 424B4 prospectus filings. The JSON data includes public offering prices, underwriting discounts, proceeds before expenses, security types being offered, underwriters (lead and co-managers), law firms, auditors, employee counts and management information (name, age, position).

```python
from sec_api import Form_S1_424B4_Api

form_s1_424B4_api = Form_S1_424B4_Api("YOUR_API_KEY")

query = {
    "query": "ticker:V",
    "from": "0",
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = form_s1_424B4_api.get_data(query)
print(response["data"])
```

> See the documentation for more details: https://sec-api.io/docs/form-s1-424b4-data-search-api

## Form C API - Crowdfunding Campaigns

Search and access Form C filings of crowdfunding campaigns from 2016 to present. The database includes information about the issuer (name, number of employees, total assets, etc), the target amount to be raised, the type of security offered, the deadline of the campaign, and more.

```python
from sec_api import FormCApi

formCApi = FormCApi("YOUR_API_KEY")

search_params = {
    "query": "id:*",
    "from": "0",
    "size": "10",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = formCApi.get_data(search_params)

print(response["data"])
```

> See the documentation for more details: https://sec-api.io/docs/form-c-crowdfunding-api

## Form D API

Search and find Form D offering filings by any filing property, e.g. total offering amount, offerings filed by hedge funds, type of securities offered and many more.

```python
from sec_api import FormDApi

formDApi = FormDApi("YOUR_API_KEY")

response = formDApi.get_data(
    {
        "query": "offeringData.offeringSalesAmounts.totalOfferingAmount:[1000000 TO *]",
        "from": "0",
        "size": "10",
        "sort": [{"filedAt": {"order": "desc"}}],
    }
)

print(response["offerings"])
```

> See the documentation for more details: https://sec-api.io/docs/form-d-xml-json-api

## Regulation A APIs

Access and search all Regulation A offering statements (Tier 1 and 2) filed with the SEC from 2015 to present. The database includes Form 1-A (offerings), Form 1-K (annual reports) and Form 1-Z (exit report) filings as well as withdrawls and amendments. Information about the issuer (total assets, debt, etc.), offering (type, total amount, offering price, auditor, etc.), and more is available.

### Search All Regulation A Filings

```python
from sec_api import RegASearchAllApi

regASearchAllApi = RegASearchAllApi("YOUR_API_KEY")

search_params = {
    "query": "filedAt:[2024-01-01 TO 2024-12-31]",
    "from": "0", # increase by 50 to fetch the next 50 results
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = regASearchAllApi.get_data(search_params)
offeringStatement = response["data"][0]

print(offeringStatement)
```

> See the documentation for more details: https://sec-api.io/docs/reg-a-offering-statements-api

### Form 1-A API

```python
from sec_api import Form1AApi

form1AApi = Form1AApi("YOUR_API_KEY")

search_params = {
    "query": "summaryInfo.indicateTier1Tier2Offering:Tier1",
    "from": "0",
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = form1AApi.get_data(search_params)
form1A = response["data"][0]

print(form1A)
```

> See the documentation for more details: https://sec-api.io/docs/reg-a-offering-statements-api

### Form 1-K API

```python
from sec_api import Form1KApi

form1KApi = Form1KApi("YOUR_API_KEY")

search_params = {
    "query": "fileNo:24R-00472",
    "from": "0",
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = form1KApi.get_data(search_params)
form1Ks = response["data"]

print(form1Ks)
```

> See the documentation for more details: https://sec-api.io/docs/reg-a-offering-statements-api

### Form 1-Z API

```python
from sec_api import Form1ZApi

form1ZApi = Form1ZApi("YOUR_API_KEY")

search_params = {
    "query": "cik:*",
    "from": "0",
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = form1ZApi.get_data(search_params)
form1Zs = response["data"]

print(form1Zs)
```

> See the documentation for more details: https://sec-api.io/docs/reg-a-offering-statements-api

## Structured Data of Material Event Disclosures under Form 8-K

### Auditor and Accountant Changes (Item 4.01)

Access and search over 25,000 change-of-accountant disclosures under Item 4.01 in SEC Form 8-K filings, spanning from 2004 to present. Access information about former and newly appointed auditors, the reason for the change, the date of the change, the type of engagement, statements regarding material weaknesses in internal controls, and more.

```python
from sec_api import Form_8K_Item_X_Api

item_X_api = Form_8K_Item_X_Api("YOUR_API_KEY")

item_4_01_request = {
    "query": "item4_01:* AND filedAt:[2024-01-01 TO 2024-12-31]",
    "from": "0",  # increase by 50 to fetch the next 50 results
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}
item_4_01_response = item_X_api.get_data(item_4_01_request)
print(item_4_01_response["data"])
```

> See the documentation for more details: https://sec-api.io/docs/form-8k-data-item4-1-search-api

### Financial Restatements & Non-Reliance on Prior Financial Results (Item 4.02)

Access and search over 8,000 financial restatements and non-reliance on prior financial results filings from 2004 to present. The database includes information about the CIK, ticker and company name the restatement is associated with, the publication date of the restatement, list of identified issues, affected reporting periods that require restatement, affected financial statement items, auditor involvement, and more.

```python
from sec_api import Form_8K_Item_X_Api

item_X_api = Form_8K_Item_X_Api("YOUR_API_KEY")

item_4_02_request = {
    "query": "item4_02:* AND filedAt:[2024-01-01 TO 2024-12-31]",
    "from": "0",
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}
item_4_02_response = item_X_api.get_data(item_4_02_request)
print(item_4_02_response["data"])
```

> See the documentation for more details: https://sec-api.io/docs/form-8k-data-search-api

### Changes of Directors, Executives, Board Members and Compensation Plans (Item 5.02)

Access and search over 250,000 changes of directors, executives, board members and compensation plans disclosures under Item 5.02 in SEC Form 8-K filings, spanning from 2004 to present. The database includes information about the CIK, ticker and company name the change is associated with, the publication date of the change, the name of the director, her/his age, position, academic affiliations, compensation details, committee memberships, and more.

```python
from sec_api import Form_8K_Item_X_Api

item_X_api = Form_8K_Item_X_Api("YOUR_API_KEY")

item_5_02_request = {
    "query": "item5_02:* AND filedAt:[2024-01-01 TO 2024-12-31]",
    "from": "0",
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}
item_5_02_response = item_X_api.get_data(item_5_02_request)
print(item_5_02_response["data"])
```

> See the documentation for more details: https://sec-api.io/docs/form-8k-data-item5-2-search-api

## Directors & Board Members Data API

Access and search the entire database of all directors and board members of all publicly listed companies on US stock exchanges. The database includes information about the CIK, ticker and company name the director is associated with, the name of the director, her/his age, position, director class, date of first election, independence status, committee memberships as well as qualifications and experiences.

```python
from sec_api import DirectorsBoardMembersApi

directorsBoardMembersApi = DirectorsBoardMembersApi("YOUR_API_KEY")

query = {
    "query": "ticker:AMZN",
    "from": 0,
    "size": 50,
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = directorsBoardMembersApi.get_data(query)
print(response["data"])
```

> See the documentation for more details: https://sec-api.io/docs/directors-and-board-members-data-api

## Executive Compensation Data API

The API provides standardized compensation data of all key executives as reported in SEC filing DEF 14A. The dataset is updated in real-time.

You can search compensation data by 13 parameters, such as company ticker, executive name & position, annual salary, option awards and more.

```python
from sec_api import ExecCompApi

execCompApi = ExecCompApi("YOUR_API_KEY")

# Get data by ticker
result_ticker = execCompApi.get_data("TSLA")

# Get data by CIK
result_cik = execCompApi.get_data("789019")

# List all exec compensations of CIK 70858 for year 2020 and 2019
# Sort result by year first, by name second
query = {
    "query": "cik:70858 AND (year:2020 OR year:2019)",
    "from": "0",
    "size": "200",
    "sort": [{"year": {"order": "desc"}}, {"name.keyword": {"order": "asc"}}],
}
result_query = execCompApi.get_data(query)
```

### Response Example

```json
[
  {
    "id": "8e9177e3bcdb30ada8d092c195bd9d63",
    "cik": "1318605",
    "ticker": "TSLA",
    "name": "Andrew Baglino",
    "position": "SVP, Powertrain and Energy Engineering",
    "year": 2020,
    "salary": 283269,
    "bonus": 0,
    "stockAwards": 0,
    "optionAwards": 46261354,
    "nonEquityIncentiveCompensation": 0,
    "changeInPensionValueAndDeferredEarnings": 0,
    "otherCompensation": 0,
    "total": 46544623
  }
  // and many more
]
```

> See the documentation for more details: https://sec-api.io/docs/executive-compensation-api

## Outstanding Shares & Public Float API

The Float API returns the number of outstanding shares and public float of any publicly traded company listed on US exchanges. The dataset includes the most recently reported number of outstanding shares and float as well as historical data. If a company registered multiple share classes, the API returns the number of shares outstanding of each class.

```python
from sec_api import FloatApi

floatApi = FloatApi("YOUR_API_KEY")

response = floatApi.get_float(ticker="GOOGL")
print(response["data"])

response = floatApi.get_float(cik="1318605")
print(response["data"])
```

> See the documentation for more details: https://sec-api.io/docs/outstanding-shares-float-api

### Response Example | Float API

```json
{
  "data": [
    {
      "tickers": ["GOOGL", "GOOG"],
      "cik": "1652044",
      "reportedAt": "2023-02-02T21:23:45-05:00",
      "periodOfReport": "2022-12-31",
      "float": {
        "outstandingShares": [
          {
            "period": "2023-01-26",
            "shareClass": "CommonClassA",
            "value": 5956000000
          },
          {
            "period": "2023-01-26",
            "shareClass": "CommonClassB",
            "value": 883000000
          },
          {
            "period": "2023-01-26",
            "shareClass": "CapitalClassC",
            "value": 5968000000
          }
        ],
        "publicFloat": [
          {
            "period": "2022-06-30",
            "shareClass": "",
            "value": 1256100000000
          }
        ]
      },
      "sourceFilingAccessionNo": "0001652044-23-000016",
      "id": "4a29432e1345e30a01e4aa10a2b57b62"
    }
    // and more...
  ]
}
```

## Subsidiary API

```python
from sec_api import SubsidiaryApi

subsidiaryApi = SubsidiaryApi("YOUR_API_KEY")

query = {
    "query": "ticker:TSLA",
    "from": "0",
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = subsidiaryApi.get_data(query)

print(response["data"])
```

> See the documentation for more details: https://sec-api.io/docs/subsidiary-api

### Response Example | Subsidiary API

```json
{
  "data": [
    {
      "id": "6838a63b29128e116bde65c885282667",
      "accessionNo": "0000950170-23-001409",
      "filedAt": "2023-01-30T21:29:15-05:00",
      "cik": "1318605",
      "ticker": "TSLA",
      "companyName": "Tesla, Inc.",
      "subsidiaries": [
        {
          "name": "Alabama Service LLC",
          "jurisdiction": "Delaware"
        }
        {
          "name": "Alset Warehouse GmbH",
          "jurisdiction": "Germany"
        },
        {
          "name": "BT Connolly Storage, LLC",
          "jurisdiction": "Texas"
        },
        {
          "name": "Fotovoltaica GI 4, S. de R.L. de C.V.",
          "jurisdiction": "Mexico"
        },
        // ... more subsidiaries
      ]
    },
    // ... more historical lists of subsidiaries
  ]
}
```

## SEC Enforcement Actions Database API

Access and search SEC enforcement actions published from 1997 to present. The database includes information about the parties involved in the action, nature of charges and complaints, penalty amounts, requested reliefs, violated rules and regulations, and more.

```python
from sec_api import SecEnforcementActionsApi

enforcementActionsApi = SecEnforcementActionsApi("YOUR_API_KEY")

search_params = {
    "query": "releasedAt:[2024-01-01 TO 2024-12-31]",
    "from": "0",
    "size": "50",
    "sort": [{"releasedAt": {"order": "desc"}}],
}

response = enforcementActionsApi.get_data(search_params)
print(response["data"])
```

> See the documentation for more details: https://sec-api.io/docs/sec-enforcement-actions-database-api

## SEC Litigation Releases Database API

Access and search the SEC Litigation Releases database. The database includes metadata and extracted structured data from all SEC Litigation Releases filed from 1995 to present.

```python
from sec_api import SecLitigationsApi

secLitigationsApi = SecLitigationsApi("YOUR_API_KEY")

searchRequest = {
    "query": "releasedAt:[2024-01-01 TO 2024-12-31]",
    "from": "0",
    "size": "50",
    "sort": [{"releasedAt": {"order": "desc"}}],
}

response = secLitigationsApi.get_data(searchRequest)
print(response["data"])
```

> See the documentation for more details: https://sec-api.io/docs/sec-litigation-releases-database-api

## SEC Administrative Proceedings Database API

Access and search all 18,000+ administrative proceedings filed by the SEC from 1995 to present. The database includes information about respondents (name, CIK, ticker), type of proceeding, publication dates, complaints and orders, violated rules and regulations, disgorgement amounts, penalties, and more.

```python
from sec_api import SecAdministrativeProceedingsApi

adminProceedingsApi = SecAdministrativeProceedingsApi("YOUR_API_KEY")

searchRequest = {
    "query": "releasedAt:[2024-01-01 TO 2024-12-31]",
    "from": "0",
    "size": "50",
    "sort": [{"releasedAt": {"order": "desc"}}],
}

response = adminProceedingsApi.get_data(searchRequest)
print(response["data"])
```

> See the documentation for more details: https://sec-api.io/docs/sec-administrative-proceedings-database-api

## AAER Database API

Access and search the Accounting and Auditing Enforcement Releases (AAER) database. The database includes all AAERs filed from 1997 to present.

```python
from sec_api import AaerApi

aaerApi = AaerApi("YOUR_API_KEY")

query = {
    "query": "dateTime:[2012-01-01 TO 2020-12-31]",
    "from": "0",
    "size": "50",
    "sort": [{"dateTime": {"order": "desc"}}],
}

response = aaerApi.get_data(query)
print(response["data"])
```

> See the documentation for more details: https://sec-api.io/docs/aaer-database-api

## SRO Filings Database API

Access and search all SRO filings published from 1995 to present. The database includes more than 30,000 SRO filings from all types of organizations, including National Securities Exchanges (NYSE, NASDAQ, CBOE, etc.), Joint Industry Plans, FINRA, Futures Exchanges (CME, CBOT, etc.), and more.

```python
from sec_api import SroFilingsApi

sroFilingsApi = SroFilingsApi("YOUR_API_KEY")

query = {
    "query": "sro:NASDAQ",
    "from": "0",
    "size": "10",
    "sort": [{"issueDate": {"order": "desc"}}],
}

response = sroFilingsApi.get_data(query)
print(response["data"])
```

> See the documentation for more details: https://sec-api.io/docs/sro-filings-database-api

## CUSIP/CIK/Ticker Mapping API

Resolve a CUSIP, CIK, ticker symbol or company name to a set of standardized company details. Listing companies by exchange, sector and industry is also supported.

Map any of the following parameters to company details:

- CUSIP
- CIK
- Ticker
- Company name
- Exchange
- Sector
- Industry

The function returns an array of all matching companies in JSON format. For example, a look up of the ticker `IBM` returns multiple matches including `IBMD` and `IBME`.

A company object includes the following properties:

- `name` (string) - the name of the company, e.g. Tesla Inc
- `ticker` (string) - the ticker symbol of the company.
- `cik` (string) - the CIK of the company. Trailing zeros are removed.
- `cusip` (string) - one or multiple CUSIPs linked to the company. Multiple CUSIPs are delimited by space, e.g. "054748108 92931L302 92931L401"
- `exchange` (string) - the main exchange the company is listed on, e.g. NASDAQ
- `isDelisted` (boolean) - true if the company is no longer listed, false otherwise.
- `category` (string) - the security category, e.g. "Domestic Common Stock"
- `sector` (string) - the sector of the company, e.g. "Consumer Cyclical"
- `industry` (string) - the industry of the company, e.g. "Auto Manufacturers"
- `sic` (string) - four-digit SIC code, e.g. "3711"
- `sicSector` (string) - SIC sector name of the company, e.g. "Manufacturing"
- `sicIndustry` (string) - SIC industry name of the company, e.g. "Motor Vehicles & Passenger Car Bodies"
- `currency` (string) - operating currency of the company, e.g. "USD"
- `location` (string) - location of the company's headquarters
- `id` (string) - unique internal ID of the company, e.g. "e27d6e9606f216c569e46abf407685f3"

Response type: `JSON`

### Usage

```python
from sec_api import MappingApi

mappingApi = MappingApi(api_key="YOUR_API_KEY")

result1 = mappingApi.resolve("ticker", "TSLA")
result2 = mappingApi.resolve("cik", "1318605")
result3 = mappingApi.resolve("cusip", "88160R101")
result4 = mappingApi.resolve("exchange", "NASDAQ")
```

#### Response Example

```json
[
  {
    "name": "Tesla Inc",
    "ticker": "TSLA",
    "cik": "1318605",
    "cusip": "88160R101",
    "exchange": "NASDAQ",
    "isDelisted": false,
    "category": "Domestic Common Stock",
    "sector": "Consumer Cyclical",
    "industry": "Auto Manufacturers",
    "sic": "3711",
    "sicSector": "Manufacturing",
    "sicIndustry": "Motor Vehicles & Passenger Car Bodies",
    "famaSector": "",
    "famaIndustry": "Automobiles and Trucks",
    "currency": "USD",
    "location": "California; U.S.A",
    "id": "e27d6e9606f216c569e46abf407685f3"
  }
]
```

> See the documentation for more details: https://sec-api.io/docs/mapping-api

## EDGAR Entities Database

Access information on over 800,000 EDGAR filing entities that have filed with the SEC since 1994. The database includes information about the CIK, IRS number, state of incorporation, fiscal year end, SIC code, current auditor, latest ICFR audit date, filer category, and more.

```python
edgarEntitiesApi = EdgarEntitiesApi("YOUR_API_KEY")

search_request = {
    "query": "cik:1318605",
    "from": "0",
    "size": "50",
    "sort": [{"cikUpdatedAt": {"order": "desc"}}],
}
response = edgarEntitiesApi.get_data(search_request)
print(response["data"])
```

> See the documentation for more details: https://sec-api.io/docs/edgar-entities-database-api

## Proxy Support

In certain cases, your corporate IT infrastructure may encounter issues with HTTPS requests, leading to SSL certificate errors. To resolve this, HTTP and HTTPS proxies can be passed into all API wrappers as shown in the example below. If you're unsure about which proxies to use, please consult your company's IT administrator.

```python
from sec_api import QueryApi, RenderApi, ...

proxies = {
  "http": "http://your-proxy.com",
  "https": "https://your-proxy.com",
}

queryApi = QueryApi(api_key="YOUR_API_KEY", proxies=proxies)
renderApi = RenderApi(api_key="YOUR_API_KEY", proxies=proxies)
```

## Query API Response Format

- `accessionNo` (string) - Accession number of filing, e.g. 0000028917-20-000033
- `cik` (string) - CIK of the filing issuer. Important: trailing `0` are removed.
- `ticker` (string) - Ticker of company, e.g. AMOT. A ticker is not available when non-publicly traded companies report filings (e.g. form 4 reported by directors). Please contact us if you find filings that you think should have tickers (but don't).
- `companyName` (string) - Name of company, e.g. Allied Motion Technologies Inc
- `companyNameLong` (string) - Long version of company name including the filer type (Issuer, Filer, Reporting), e.g. ALLIED MOTION TECHNOLOGIES INC (0000046129) (Issuer)
- `formType` (string) - sec.gov form type, e.g 10-K. [See the list of supported form types here.](https://sec-api.io/#list-of-sec-form-types)
- `description` (string) - Description of the form, e.g. Statement of changes in beneficial ownership of securities
- `linkToFilingDetails` (string) - Link to HTML, XML or PDF version of the filing.
- `linkToTxt` (string) - Link to the plain text version of the filing. This file can be multiple MBs large.
- `linkToHtml` (string) - Link to index page of the filing listing all exhibits and the original HTML file.
- `linkToXbrl` (string, optional) - Link to XBRL version of the filing (if available).
- `filedAt` (string) - The date (format: YYYY-MM-DD HH:mm:SS TZ) the filing was filed, eg 2019-12-06T14:41:26-05:00.
- `periodOfReport` (string, if reported) - Period of report, e.g. 2021-06-08
- `effectivenessDate` (string, if reported) - Effectiveness date, e.g. 2021-06-08
- `registrationForm` (string, if reported) - Registration form as reported on EFFECT forms, e.g. S-1
- `referenceAccessionNo` (string, if reported) - Reference accession number as reported on EFFECT forms, e.g. 0001213900-22-001446
- `items` (array of strings, if reported) - Items represents an array of item strings as reported on form 8-K, 8-K/A, D, D/A, ABS-15G, ABS-15G/A, 1-U, 1-U/A. For example: `["Item 3.02: Unregistered Sales of Equity Securities", "Item 9.01: Financial Statements and Exhibits"]`
- `groupMembers` (array, if reported) - Group members represents an array of member strings as reported on SC 13G, SC 13G/A, SC 13D, SC 13D/A filings, e.g. `[ "ALEC N. LITOWITZMAGNETAR CAPITAL PARTNERS LPSUPERNOVA MANAGEMENT LLC" ]`
- `id` (string) - Unique ID of the filing.
- `entities` (array) - A list of all entities referred to in the filing. The first item in the array always represents the filing issuer. Each array element is an object with the following keys:
  - `companyName` (string) - Company name of the entity, e.g. DILLARD'S, INC. (Issuer)
  - `cik` (string) - CIK of the entity. Trailing 0 are not removed here, e.g. 0000028917
  - `irsNo` (string, optional) - IRS number of the entity, e.g. 710388071
  - `stateOfIncorporation` (string, optional) - State of incorporation of entity, e.g. AR
  - `fiscalYearEnd` (string, optional) - Fiscal year end of the entity, e.g. 0201
  - `sic` (string, optional) - SIC of the entity, e.g. 5311 Retail-Department Stores
  - `type` (string, optional) - Type of the filing being filed. Same as formType, e.g. 4
  - `act` (string, optional) - The SEC act pursuant to which the filing was filed, e.g. 34
  - `fileNo` (string, optional) - Filer number of the entity, e.g. 001-06140
  - `filmNo` (string, optional) - Film number of the entity, e.g. 20575664
- `documentFormatFiles` (array) - An array listing all primary files of the filing. The first item of the array is always the filing itself. The last item of the array is always the TXT version of the filing. All other items can represent exhibits, press releases, PDF documents, presentations, graphics, XML files, and more. An array item is represented as follows:
  - `sequence` (string, optional) - The sequence number of the filing, e.g. 1
  - `description` (string, optional) - Description of the file, e.g. EXHIBIT 31.1
  - `documentUrl` (string) - URL to the file on SEC.gov
  - `type` (string, optional) - Type of the file, e.g. EX-32.1, GRAPHIC or 10-Q
  - `size` (string, optional) - Size of the file, e.g. 6627216
- `dataFiles` (array) - List of data files (filing attachments, exhibits, XBRL files) attached to the filing.
  - `sequence` (string) - Sequence number of the file, e.g. 6
  - `description` (string) - Description of the file, e.g. XBRL INSTANCE DOCUMENT
  - `documentUrl` (string) - URL to the file on SEC.gov
  - `type` (string, optional) - Type of the file, e.g. EX-101.INS, EX-101.DEF or EX-101.PRE
  - `size` (string, optional) - Size of the file, e.g. 6627216
- `seriesAndClassesContractsInformation` (array) - List of series and classes/contracts information
  - `series` (string) - Series ID, e.g. S000001297
  - `name` (string) - Name of entity, e.g. PRUDENTIAL ANNUITIES LIFE ASSUR CORP VAR ACCT B CL 1 SUB ACCTS
  - `classesContracts` (array) - List of classes/contracts. Each list item has the following keys:
    - `classContract` (string) - Class/Contract ID, e.g. C000011787
    - `name` (string) - Name of class/contract entity, e.g. Class L
    - `ticker` (string) - Ticker class/contract entity, e.g. URTLX

### 13F Institutional Ownerships

13F filings report institutional ownerships. Each 13F filing has an attribute `holdings` (array). An array item in holdings represents one holding and has the following attributes:

- `nameOfIssuer` (string) - Name of issuer, e.g. MICRON TECHNOLOGY INC
- `titleOfClass` (string) - Title of class, e.g. COM
- `cusip` (string) - CUSIP of security, e.g. 98850P109
- `value` (integer) - Absolute holding value in $, e.g. 18000. Note: `value` doesn't have to be multiplied by 1000 anymore. It's done by our API automatically.
- `shrsOrPrnAmt` (object)
  - `sshPrnamt` (integer) - Shares or PRN AMT, e.g. 345
  - `sshPrnamtType` (string) - Share/PRN type, e.g. "SH"
- `putCall` (string, optional) - Put / Call, e.g. Put
- `investmentDiscretion` (string) - Investment discretion, e.g. "SOLE"
- `otherManager` (string, optional) - Other manager, e.g. 7
- `votingAuthority` (object)
  - `Sole` (integer) - Sole, e.g. 345
  - `Shared` (integer) - Shared, e.g. 345
  - `None` (integer) - None, e.g. 345

### Query API Example JSON Response

```json
{
  "id": "79ad9e452ea42402df4fe55c636191d6",
  "accessionNo": "0001213900-21-032169",
  "cik": "1824149",
  "ticker": "JOFF",
  "companyName": "JOFF Fintech Acquisition Corp.",
  "companyNameLong": "JOFF Fintech Acquisition Corp. (Filer)",
  "formType": "10-Q",
  "description": "Form 10-Q - Quarterly report [Sections 13 or 15(d)]",
  "filedAt": "2021-06-11T17:25:44-04:00",
  "linkToTxt": "https://www.sec.gov/Archives/edgar/data/1824149/000121390021032169/0001213900-21-032169.txt",
  "linkToHtml": "https://www.sec.gov/Archives/edgar/data/1824149/000121390021032169/0001213900-21-032169-index.htm",
  "linkToXbrl": "",
  "linkToFilingDetails": "https://www.sec.gov/Archives/edgar/data/1824149/000121390021032169/f10q0321_jofffintech.htm",
  "entities": [
    {
      "companyName": "JOFF Fintech Acquisition Corp. (Filer)",
      "cik": "1824149",
      "irsNo": "852863893",
      "stateOfIncorporation": "DE",
      "fiscalYearEnd": "1231",
      "type": "10-Q",
      "act": "34",
      "fileNo": "001-40005",
      "filmNo": "211012398",
      "sic": "6770 Blank Checks"
    }
  ],
  "documentFormatFiles": [
    {
      "sequence": "1",
      "description": "QUARTERLY REPORT",
      "documentUrl": "https://www.sec.gov/Archives/edgar/data/1824149/000121390021032169/f10q0321_jofffintech.htm",
      "type": "10-Q",
      "size": "274745"
    },
    {
      "sequence": "2",
      "description": "CERTIFICATION",
      "documentUrl": "https://www.sec.gov/Archives/edgar/data/1824149/000121390021032169/f10q0321ex31-1_jofffintech.htm",
      "type": "EX-31.1",
      "size": "12209"
    },
    {
      "sequence": "3",
      "description": "CERTIFICATION",
      "documentUrl": "https://www.sec.gov/Archives/edgar/data/1824149/000121390021032169/f10q0321ex31-2_jofffintech.htm",
      "type": "EX-31.2",
      "size": "12220"
    },
    {
      "sequence": "4",
      "description": "CERTIFICATION",
      "documentUrl": "https://www.sec.gov/Archives/edgar/data/1824149/000121390021032169/f10q0321ex32-1_jofffintech.htm",
      "type": "EX-32.1",
      "size": "4603"
    },
    {
      "sequence": "5",
      "description": "CERTIFICATION",
      "documentUrl": "https://www.sec.gov/Archives/edgar/data/1824149/000121390021032169/f10q0321ex32-2_jofffintech.htm",
      "type": "EX-32.2",
      "size": "4607"
    },
    {
      "sequence": " ",
      "description": "Complete submission text file",
      "documentUrl": "https://www.sec.gov/Archives/edgar/data/1824149/000121390021032169/0001213900-21-032169.txt",
      "type": " ",
      "size": "2344339"
    }
  ],
  "dataFiles": [
    {
      "sequence": "6",
      "description": "XBRL INSTANCE FILE",
      "documentUrl": "https://www.sec.gov/Archives/edgar/data/1824149/000121390021032169/joff-20210331.xml",
      "type": "EX-101.INS",
      "size": "248137"
    },
    {
      "sequence": "7",
      "description": "XBRL SCHEMA FILE",
      "documentUrl": "https://www.sec.gov/Archives/edgar/data/1824149/000121390021032169/joff-20210331.xsd",
      "type": "EX-101.SCH",
      "size": "43550"
    },
    {
      "sequence": "8",
      "description": "XBRL CALCULATION FILE",
      "documentUrl": "https://www.sec.gov/Archives/edgar/data/1824149/000121390021032169/joff-20210331_cal.xml",
      "type": "EX-101.CAL",
      "size": "21259"
    },
    {
      "sequence": "9",
      "description": "XBRL DEFINITION FILE",
      "documentUrl": "https://www.sec.gov/Archives/edgar/data/1824149/000121390021032169/joff-20210331_def.xml",
      "type": "EX-101.DEF",
      "size": "182722"
    },
    {
      "sequence": "10",
      "description": "XBRL LABEL FILE",
      "documentUrl": "https://www.sec.gov/Archives/edgar/data/1824149/000121390021032169/joff-20210331_lab.xml",
      "type": "EX-101.LAB",
      "size": "309660"
    },
    {
      "sequence": "11",
      "description": "XBRL PRESENTATION FILE",
      "documentUrl": "https://www.sec.gov/Archives/edgar/data/1824149/000121390021032169/joff-20210331_pre.xml",
      "type": "EX-101.PRE",
      "size": "186873"
    }
  ],
  "seriesAndClassesContractsInformation": [],
  "periodOfReport": "2021-03-31",
  "effectivenessDate": "2021-03-31"
}
```

## Contact

Let us know how we can improve the library or if you have any feature suggestions. We're happy to implement them.

support@sec-api.io
