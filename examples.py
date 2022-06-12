from sec_api.index import RenderApi, XbrlApi, ExtractorApi, MappingApi, ExecCompApi

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
