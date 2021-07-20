from sec_api.index import XbrlApi

xbrlApi = XbrlApi("YOUR_API_KEY")

# 10-K HTM File URL example
xbrl_json_1 = xbrlApi.xbrl_to_json(
    htm_url="https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/aapl-20200926.htm"
)

print(xbrl_json_1["StatementsOfIncome"])
print(xbrl_json_1["BalanceSheets"])
print(xbrl_json_1["StatementsOfCashFlows"])

# 10-K XBRL File URL example
xbrl_json_2 = xbrlApi.xbrl_to_json(
    xbrl_url="https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231_htm.xml"
)

# 10-K XBRL File URL example
xbrl_json_3 = xbrlApi.xbrl_to_json(accession_no="0001564590-21-004599")
