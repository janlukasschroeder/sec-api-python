from sec_api.index import (
    RenderApi,
    PdfGeneratorApi,
    XbrlApi,
    ExtractorApi,
    #
    FormAdvApi,
    #
    InsiderTradingApi,
    Form144Api,
    Form13FHoldingsApi,
    Form13FCoverPagesApi,
    FormNportApi,
    Form13DGApi,
    #
    FormNPXApi,
    #
    Form_S1_424B4_Api,
    FormCApi,
    FormDApi,
    RegASearchAllApi,
    Form1AApi,
    Form1KApi,
    Form1ZApi,
    #
    Item_4_02_Api,
    Form_8K_Item_X_Api,
    #
    DirectorsBoardMembersApi,
    ExecCompApi,
    SubsidiaryApi,
    FloatApi,
    #
    SecEnforcementActionsApi,
    SecLitigationsApi,
    SecAdministrativeProceedingsApi,
    AaerApi,
    SroFilingsApi,
    #
    MappingApi,
    EdgarEntitiesApi,
)

#
# Render API
#
"""
from sec_api import RenderApi

renderApi = RenderApi(api_key="YOUR_API_KEY")

# example URLs: SEC filings, exhibits, images, Excel sheets, PDFs
url_8k_html = "https://www.sec.gov/Archives/edgar/data/1045810/000104581023000014/nvda-20230222.htm"
url_8k_txt = "https://www.sec.gov/Archives/edgar/data/1045810/000104581023000014/0001045810-23-000014.txt"
url_exhibit99 = "https://www.sec.gov/Archives/edgar/data/1045810/000104581023000014/q4fy23pr.htm"
url_xbrl_instance = "https://www.sec.gov/Archives/edgar/data/1045810/000104581023000014/nvda-20230222_htm.xml"
url_excel_file = "https://www.sec.gov/Archives/edgar/data/1045810/000104581023000014/Financial_Report.xlsx"
url_pdf_file = "https://www.sec.gov/Archives/edgar/data/1798925/999999999724004095/filename1.pdf"
url_image_file = "https://www.sec.gov/Archives/edgar/data/1424404/000106299324017776/form10kxz001.jpg"

filing_8k_html = renderApi.get_file(url_8k_html)
filing_8k_txt = renderApi.get_file(url_8k_txt)
exhibit99 = renderApi.get_file(url_exhibit99)
xbrl_instance = renderApi.get_file(url_xbrl_instance)

# use .get_file() and set return_binary=True
# to get non-text files such as images, PDFs, etc.
excel_file = renderApi.get_file(url_excel_file, return_binary=True)
pdf_file = renderApi.get_file(url_pdf_file, return_binary=True)
image_file = renderApi.get_file(url_image_file, return_binary=True)

# save files to disk
with open("filing_8k_html.htm", "wb") as f:
    f.write(filing_8k_html.encode("utf-8"))
with open("pdf_file.pdf", "wb") as f:
    f.write(pdf_file)
with open("image.jpg", "wb") as f:
    f.write(image_file)
# """

#
# PDF Generator API
#
"""
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
# Directors & Board Members API Example
#
"""
directorsBoardMembersApi = DirectorsBoardMembersApi("YOUR_API_KEY")

query = {
    "query": "ticker:AMZN",
    "from": 0,
    "size": 50,
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = directorsBoardMembersApi.get_data(query)
print(response["data"])
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
        "query": "issuer.tradingSymbol:TSLA",
        "from": "0",
        "size": "50",
        "sort": [{"filedAt": {"order": "desc"}}],
    }
)

print(insider_trades["transactions"])
# """


#
# Form 144 API Example
#
"""
form144Api = Form144Api("YOUR_API_KEY")

search_params = {
    "query": "entities.ticker:TSLA",
    "from": "0",
    "size": "1",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = form144Api.get_data(search_params)

print(response["data"])
# """


#
# Form 13F Holdings API Example
#
"""
form13FHoldingsApi = Form13FHoldingsApi("YOUR_API_KEY")

search_params = {
    "query": "cik:1698218",
    "from": "0",
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = form13FHoldingsApi.get_data(search_params)

print(response["data"])
# """


#
# Form 13F Cover Pages API Example
#
"""
form13FCoverPagesApi = Form13FCoverPagesApi("YOUR_API_KEY")

search_params = {
    "query": "cik:1698218",
    "from": "0",
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = form13FCoverPagesApi.get_data(search_params)

print(response["data"])
# """


#
# Form NPORT API Example
#
"""
nportApi = FormNportApi("YOUR_API_KEY")

response = nportApi.get_data(
    {
        "query": "fundInfo.totAssets:[100000000 TO *]",
        "from": "0",
        "size": "2",
        "sort": [{"filedAt": {"order": "desc"}}],
    }
)

print(response["filings"])
# """

#
# Form C API Example
#
"""
formCApi = FormCApi("YOUR_API_KEY")

search_params = {
    "query": "id:*",
    "from": "0",
    "size": "10",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = formCApi.get_data(search_params)

print(response["data"])
# """

#
# Form D API Example
#
"""
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
# """

#
# Regulation A Search All API Example
#
"""
regASearchAllApi = RegASearchAllApi("YOUR_API_KEY")

search_params = {
    "query": "filedAt:[2024-01-01 TO 2024-12-31]",
    "from": "0",  # increase by 50 to fetch the next 50 results
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = regASearchAllApi.get_data(search_params)
offeringStatement = response["data"][0]

print(offeringStatement)
# """

#
# Form 1-A API
#
"""
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
# """

#
# Form 1-K API
#
"""
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
# """

#
# Form 1-Z API
#
"""
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
# """


#
# Form ADV API Example
#
"""
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
    "query": "accessionNo:*",
    "from": "0",
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = form13DGApi.get_data(query)
print(response["filings"])
# """


#
# Form N-PX API Examples
#
"""
formNpxApi = FormNPXApi("YOUR_API_KEY")

search_params = {
    "query": "cik:884546",
    "from": "0",
    "size": "1",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = formNpxApi.get_metadata(search_params)
npx_filing_metadata = response["data"]

print(npx_filing_metadata)

accessionNo = npx_filing_metadata[0]["accessionNo"]
response = formNpxApi.get_voting_records(accessionNo)

print(response["proxyVotingRecords"][0])
# """


#
# Form S-1/424B4 API Example
#
"""
form_s1_424B4_api = Form_S1_424B4_Api("YOUR_API_KEY")

query = {
    "query": "ticker:V",
    "from": "0",
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = form_s1_424B4_api.get_data(query)
print(response["data"])
# """


#
# Subsidiary API Example
#
"""
subsidiaryApi = SubsidiaryApi("YOUR_API_KEY")

query = {
    "query": "ticker:TSLA",
    "from": "0",
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}

response = subsidiaryApi.get_data(query)
print(response["data"])
# """

#
# SEC Enforcement Actions API Example
#
"""
enforcementActionsApi = SecEnforcementActionsApi("YOUR_API_KEY")

search_params = {
    "query": "releasedAt:[2024-01-01 TO 2024-12-31]",
    "from": "0",
    "size": "50",
    "sort": [{"releasedAt": {"order": "desc"}}],
}

response = enforcementActionsApi.get_data(search_params)
print(response["data"])
# """

#
# SEC Litigation Releases API Example
#
"""
secLitigationsApi = SecLitigationsApi("YOUR_API_KEY")

query = {
    "query": "releasedAt:[2024-01-01 TO 2024-12-31]",
    "from": "0",
    "size": "50",
    "sort": [{"releasedAt": {"order": "desc"}}],
}

response = secLitigationsApi.get_data(query)
print(response["data"])
# """

#
# SEC Administrative Proceedings API Example
#
"""
adminProceedingsApi = SecAdministrativeProceedingsApi("YOUR_API_KEY")

search_params = {
    "query": "releasedAt:[2024-01-01 TO 2024-12-31]",
    "from": "0",
    "size": "50",
    "sort": [{"releasedAt": {"order": "desc"}}],
}

response = adminProceedingsApi.get_data(search_params)
print(response["data"])
# """

#
# AAER API Example
#
"""
aaerApi = AaerApi("YOUR_API_KEY")

query = {
    "query": "dateTime:[2012-01-01 TO 2020-12-31]",
    "from": "0",
    "size": "50",
    "sort": [{"dateTime": {"order": "desc"}}],
}

response = aaerApi.get_data(query)
print(response["data"])
# """


#
# SRO Filings API Example
#
"""
sroFilingsApi = SroFilingsApi("YOUR_API_KEY")

query = {
    "query": "sro:NASDAQ",
    "from": "0",
    "size": "10",
    "sort": [{"issueDate": {"order": "desc"}}],
}

response = sroFilingsApi.get_data(query)
print(response["data"])
# """

#
# Form 8-K Item 4.02 API Example
#
"""
item_4_02_api = Item_4_02_Api("YOUR_API_KEY")

query = {
    "query": "filedAt:[2010-01-01 TO 2019-12-31]",
    "from": "0",  # increase by 50 to fetch the next 50 results, e.g. 50 (=page 2), 100 (=page 3), 150 (=page 4), ...
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}
response = item_4_02_api.get_data(query)
print(response["data"])
# """

#
# Form 8-K Item X API Examples
#
"""
item_X_api = Form_8K_Item_X_Api("YOUR_API_KEY")

item_4_01_request = {
    "query": "item4_01:* AND filedAt:[2024-01-01 TO 2024-12-31]",
    "from": "0",  # increase by 50 to fetch the next 50 results, e.g. 50 (=page 2), 100 (=page 3), 150 (=page 4), ...
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}
item_4_01_response = item_X_api.get_data(item_4_01_request)
print(item_4_01_response["data"])

item_5_02_request = {
    "query": "item5_02:* AND filedAt:[2024-01-01 TO 2024-12-31]",
    "from": "0",  # increase by 50 to fetch the next 50 results, e.g. 50 (=page 2), 100 (=page 3), 150 (=page 4), ...
    "size": "50",
    "sort": [{"filedAt": {"order": "desc"}}],
}
item_5_02_response = item_X_api.get_data(item_5_02_request)
print(item_5_02_response["data"])
# """

#
# EDGAR Entities Database API Example
#
"""
edgarEntitiesApi = EdgarEntitiesApi("YOUR_API_KEY")

search_request = {
    "query": "cik:1318605",
    "from": "0",
    "size": "50",
    "sort": [{"cikUpdatedAt": {"order": "desc"}}],
}
response = edgarEntitiesApi.get_data(search_request)
print(response["data"])
# """
