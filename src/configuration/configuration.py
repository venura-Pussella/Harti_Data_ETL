# src/configuration/configuration.py

import os

# PDF data saving path
pdf_output_directory = os.path.join('data', 'pdf')

# CSV data saving path
CSV_DIR = os.path.join('data', 'csv')

# SQL Table name
SQL_TABLE_NAME = 'Food_Prices'

# SQL connection string
CONNECTION_STRING = 'mssql://BGL-DTS33\\MSSQLSERVER1/mydb?driver=ODBC+DRIVER+17+FOR+SQL+SERVER'

# Download URL
pdf_source_url = 'https://www.harti.gov.lk/index.php/en/market-information/data-food-commodities-bulletin'

# Date column
date_col = 'Date'

# MetaData line to search
metadata_line1 = '(Wholesale Prices of Rice & Subsidiary Food Crops)'

# Blob Storage connection
storage_account_key = "FAvmhCQ9RUWPiSTbghhs+eaSYXxjoGPWw7I+V+fwSbAglZaKbmw6naMLQZpJFNtpLBKSDVassRbk+AStvBqdXw=="
storage_account_name = "haristoragenew"
connect_str = "DefaultEndpointsProtocol=https;AccountName=haristoragenew;AccountKey=FAvmhCQ9RUWPiSTbghhs+eaSYXxjoGPWw7I+V+fwSbAglZaKbmw6naMLQZpJFNtpLBKSDVassRbk+AStvBqdXw==;EndpointSuffix=core.windows.net"
container_name_blob = "hartidata"

# Cosmos db connection
endpoint = "https://cosmosdbtestvj.documents.azure.com:443/"
key = "zqXrJ9iN1xvyuA5d6HeL4HPdsvpA2L7YQyNYDhhlBD5lCgKuNFjlNP9yDIaSQHo0LmlMotHXBfN0ACDb9YTkXw=="
database_name = 'exchangedetails'
container_name_cosmos = 'hartiinfo'


