from sec_api.index import (
    RenderApi,
    XbrlApi,
    ExtractorApi,
    MappingApi,
    ExecCompApi,
    InsiderTradingApi,
    FormNportApi,
    FormDApi,
    FormAdvApi,
    FloatApi,
    Form13DGApi,
    SubsidiaryApi,
)

#
# Render API
#
"""
renderApi = RenderApi("YOUR_API_KEY")

# 10-K HTM File URL example
filing_data = renderApi.get_filing(
    url="https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/aapl-20200926.htm"
)

print(filing_data)
# """

#
# XBRL-to-JSON API example
#
"""
xbrlApi = XbrlApi("YOUR_API_KEY")

# 10-K HTM File URL example
xbrl_json_1 = xbrlApi.xbrl_to_json(
    htm_url="https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/aapl-20200926.htm"
)

# print(xbrl_json_1["StatementsOfIncome"])
# print(xbrl_json_1["BalanceSheets"])
# print(xbrl_json_1["StatementsOfCashFlows"])

# 10-K XBRL File URL example
xbrl_json_2 = xbrlApi.xbrl_to_json(
    xbrl_url="https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231_htm.xml"
)

# 10-K XBRL File URL example
xbrl_json_3 = xbrlApi.xbrl_to_json(accession_no="0001564590-21-004599")

# """

#
# Extractor API Example
#
"""
extractorApi = ExtractorApi("YOUR_API_KEY")

# Tesla 10-K filing
filing_url = "https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231.htm"

section_text = extractorApi.get_section(filing_url, "1A", "text")
section_html = extractorApi.get_section(filing_url, "1A", "html")

print(section_text)
print(section_html)
# """


#
# Mapping API Example
#
"""
mappingApi = MappingApi("YOUR_API_KEY")

result = mappingApi.resolve("cik", "927355")

print(result)
# """


#
# Executive Compensation Data API Example
#
"""
execCompApi = ExecCompApi("YOUR_API_KEY")

# Get data by ticker
result_ticker = execCompApi.get_data("TSLA")

# Get data by CIK
result_cik = execCompApi.get_data("789019")

# List all exec compensations of CIK 70858 for year 2020 and 2019
# Sort result by year first, by name second
query = {
    "query": {"query_string": {"query": "cik:70858 AND (year:2020 OR year:2019)"}},
    "from": "0",
    "size": "200",
    "sort": [{"year": {"order": "desc"}}, {"name.keyword": {"order": "asc"}}],
}
result_query = execCompApi.get_data(query)


print(result_ticker)
print(result_cik)
print(result_query)
# """


#
# Insider Trading Data API Example
#
"""
insiderTradingApi = InsiderTradingApi("YOUR_API_KEY")

insider_trades = insiderTradingApi.get_data(
    {
        "query": {"query_string": {"query": "issuer.tradingSymbol:TSLA"}},
        "from": "0",
        "size": "50",
        "sort": [{"filedAt": {"order": "desc"}}],
    }
)

print(insider_trades["transactions"])
# """

#
# Form NPORT API Example
#
"""
nportApi = FormNportApi("YOUR_API_KEY")

response = nportApi.get_data(
    {
        "query": {"query_string": {"query": "fundInfo.totAssets:[100000000 TO *]"}},
        "from": "0",
        "size": "2",
        "sort": [{"filedAt": {"order": "desc"}}],
    }
)

print(response["filings"])
# """

#
# Form D API Example
#
"""
formDApi = FormDApi("YOUR_API_KEY")

response = formDApi.get_data(
    {
        "query": {
            "query_string": {
                "query": "offeringData.offeringSalesAmounts.totalOfferingAmount:[1000000 TO *]"
            }
        },
        "from": "0",
        "size": "10",
        "sort": [{"filedAt": {"order": "desc"}}],
    }
)

print(response["offerings"])
# """


#
# Form ADV API Example
#
"""
formAdvApi = FormAdvApi("YOUR_API_KEY")

response = formAdvApi.get_firms(
    {
        "query": {"query_string": {"query": "Info.FirmCrdNb:361"}},
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
        "query": {"query_string": {"query": "CrntEmps.CrntEmp.orgPK:149777"}},
        "from": "0",
        "size": "10",
        "sort": [{"id": {"order": "desc"}}],
    }
)
print(response["filings"])

response = formAdvApi.get_brochures(149777)
print(response["brochures"])
# """


#
# Float API Example
#
"""
floatApi = FloatApi("YOUR_API_KEY")

response = floatApi.get_float(ticker="TSLA")
print(response["data"])

response = floatApi.get_float(cik="1318605")
print(response["data"])
# """


#
# Form 13D/13G API Example
#
"""
form13DGApi = Form13DGApi("YOUR_API_KEY")

query = {
    "query": {"query_string": {"query": "accessionNo:*"}},
    "from": "0",
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = form13DGApi.get_data(query)
print(response["filings"])
# """


#
# Subsidiary API Example
#
"""
subsidiaryApi = SubsidiaryApi("YOUR_API_KEY")

query = {
    "query": {"query_string": {"query": "ticker:TSLA"}},
    "from": "0",
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = subsidiaryApi.get_data(query)
print(response["data"])
# """
