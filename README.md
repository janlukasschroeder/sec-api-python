# SEC API - A SEC.gov EDGAR Filings Query & Real-Time Stream API

**sec-api** is a Python package for querying the entire SEC filings corpus in real-time without the need to download filings. 
It includes:

- Query and Full-Text Search API
- Real-Time Stream API
- XBRL-to-JSON Converter API + Financial Statements
- Filing Render & Download API


# Data Coverage

- All +18 million SEC EDGAR filings dating back to 1993
- **All +150 filing types** are supported, eg 10-Q, 10-K, 4, 8-K, 13-F, S-1, 424B4 and many more.
  [See the list of supported form types here.](https://sec-api.io/list-of-sec-filing-types)
- Newly published filings are accessible in real-time
- XBRL-to-JSON converter and parser API. Extract standardized financial statements from any 10-K and 10-Q filing.
- 13F holdings API included. Monitor all institutional ownerships in real-time.
- Every filing is **mapped to a CIK and ticker**
- All filings in JSON - **no XBRL/XML**

Data source: [sec.gov](https://www.sec.gov/edgar/searchedgar/companysearch.html)

# Overview

- The query API gives access to all over 18 million SEC Edgar filings of **over 8000** 
publicly listed companies, ETFs, hedge funds, mutual funds, and investors dating back to 1993.
- Connect to the real-time stream API to receive new filings as soon as they are published on SEC EDGAR
- The full-text search API allows you to search the full text of all filings submitted since 2001. 
The full text of a filing includes all data in the filing itself as well as all attachments (such as exhibits) to the filing.
- Free API key available on [sec-api.io](https://sec-api.io)

See the official documentation for more: [sec-api.io/docs](https://sec-api.io/docs)

# Installation

```bash
pip install sec-api
```

Get your free API key on [sec-api.io](https://sec-api.io) and replace `YOUR_API_KEY` with it.


# SEC EDGAR Filings Query API

The query API allows you to search and filter all 18 million filings published on SEC EDGAR.

---

The example below retrieves all 10-Q filings filed by TSLA in 2020.

```python
from sec_api import QueryApi

queryApi = QueryApi(api_key="YOUR_API_KEY")

query = {
  "query": { "query_string": { 
      "query": "ticker:TSLA AND filedAt:{2020-01-01 TO 2020-12-31} AND formType:\"10-Q\"" 
    } },
  "from": "0",
  "size": "10",
  "sort": [{ "filedAt": { "order": "desc" } }]
}

filings = queryApi.get_filings(query)

print(filings)
```

Fetch most recent 8-Ks with item 9.01

```python
query = {
  "query": { "query_string": { 
      "query": "formType:\"8-K\" AND description:\"9.01\""
    } },
  "from": "0",
  "size": "10",
  "sort": [{ "filedAt": { "order": "desc" } }]
}

filings = queryApi.get_filings(query)
```

Fetch most recent 13F filings that hold Tesla

```python
query = {
  "query": { "query_string": { 
      "query": "formType:\"13F\" AND holdings.cusip:88160R101"
    } },
  "from": "0",
  "size": "10",
  "sort": [{ "filedAt": { "order": "desc" } }]
}

filings = queryApi.get_filings(query)
```

> See the documentation for more details: https://sec-api.io/docs/query-api



# SEC EDGAR Filings Real-Time Stream API

The stream API provides a live stream (aka feed) of newly published filings on SEC EDGAR.
A new filing is sent to your connected client as soon as its published.

---

Install the `socketio` client:

```bash
pip install python-engineio==3.14.2 python-socketio[client]==4.6.0
```

Run the example script below. Get your free API key on [sec-api.io](https://sec-api.io)
  and replace `YOUR_API_KEY` with it.

```python
import socketio

sio = socketio.Client()

@sio.on("connect", namespace="/all-filings")
def on_connect():
    print("Connected to https://api.sec-api.io:3334/all-filings")

@sio.on("filing", namespace="/all-filings")
def on_filings(filing):
    print(filing)

sio.connect("https://api.sec-api.io:3334?apiKey=YOUR_API_KEY", namespaces=["/all-filings"], transports=["websocket"])
sio.wait()
```

# Full-Text Search API

Full-text search allows you to search the full text of all EDGAR filings submitted since 2001. 
The full text of a filing includes all data in the filing itself as well as all attachments (such as exhibits) to the filing.

---

The example below returns all 8-K and 10-Q filings and their exhibits, filed between 01-01-2021 and 14-06-2021, 
that include the exact phrase "LPCN 1154".


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


# XBRL-To-JSON Converter API

Parse and standardize any XBRL and convert it to JSON or pandas dataframes. Extract financial statements and meta data from 10-K and 10-Q filings.

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

## Income Statement - Example Item

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

## Usage

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

## Example Response

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



# Filing Render & Download API

Used to download any filing or exhibit. You can process the downloaded filing in memory or save the filing to your hard drive.

```python
from sec_api import RenderApi

renderApi = RenderApi(api_key="YOUR_API_KEY")

url = "https://www.sec.gov/Archives/edgar/data/1662684/000110465921082303/tm2119986d1_8k.htm"

filing = renderApi.get_filing(url)

print(filing)
```

> See the documentation for more details: https://sec-api.io/docs/sec-filings-render-api


# Response Format

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


## 13F Institutional Ownerships

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

## Example JSON Response

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

# Contact

Let me know how I can improve the library or if you have any feature
suggestions. I'm happy to implement them.

support@sec-api.io
