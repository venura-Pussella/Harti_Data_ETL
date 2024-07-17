# src/configuration/configuration.py

import os

# PDF data saving path
pdf_output_directory = os.path.join('data', 'pdf')

# CSV data saving path
CSV_DIR = os.path.join('data', 'csv')

# Proxy server 

# proxies = {
#     'https': 'https://202.124.188.98:3128'
# }

# SQL Table name
# SQL_TABLE_NAME = 'Food_Prices'

# # SQL connection string
# CONNECTION_STRING = 'mssql://BGL-DTS33\\MSSQLSERVER1/mydb?driver=ODBC+DRIVER+17+FOR+SQL+SERVER'

# Download URL
pdf_source_url = 'https://www.harti.gov.lk/index.php/en/market-information/data-food-commodities-bulletin'

# Date column
date_col = 'Date'

# MetaData line to search
metadata_line1 = '(Wholesale Prices of Rice & Subsidiary Food Crops)'

# Blob Storage connection
storage_account_key = "xGizEMa9uTLu+SJgIErKVMbnVzU1Ow1WeP8cc1cnX1tJFMUUMwPuqw1v8uOJ8PUExFFVXWvNpfhy+ASt2bXIYw=="
storage_account_name = "bgaiservice"
connect_str = "DefaultEndpointsProtocol=https;AccountName=bgaiservice;AccountKey=xGizEMa9uTLu+SJgIErKVMbnVzU1Ow1WeP8cc1cnX1tJFMUUMwPuqw1v8uOJ8PUExFFVXWvNpfhy+ASt2bXIYw==;EndpointSuffix=core.windows.net"
container_name_blob = "harti-food-data-page-1"

# Cosmos db connection
endpoint = "https://db-brownschatbot.documents.azure.com:443/"
key = "vCXyyEyOA9xo08aiSUbKHjT5F4POHwe9ZXmmP7u8uBa0q4mu2lxDJZ9yDpETDQhT6D7cxp3c4qfhACDboABmjw=="
database_name = 'db_conversation_history'
container_name_cosmos = 'Harti-Data-History'


