# main.py
import asyncio
import platform
from src import logger
from src.connector.blob import upload_to_blob
from src.connector.cosmos_db import write_harti_data_to_cosmosdb
from src.configuration.configuration import pdf_source_url, metadata_line1
from src.pipeline1.lists_to_dataframe import create_dataframe
from src.pipeline1.data_transformer import transform_dataframe
from src.pipeline1.text_to_lists import parse_text, get_patterns
from src.pipeline1.metadata_reader import find_line_with_metadata
from src.pipeline1.data_format_converter import dataframe_to_csv_string, convert_dataframe_to_cosmos_format
from src.pipeline1.text_extractor import get_latest_pdf_link, download_pdf_as_bytes, extract_text_from_first_page

async def main():

    try:
        logger.info(">>>> Starting the data extraction process <<<<")

        # Download the latest PDF
        latest_pdf_link = get_latest_pdf_link(pdf_source_url)
        if latest_pdf_link:
            logger.info(f"Latest PDF link: {latest_pdf_link}")
            pdf_bytes = download_pdf_as_bytes(latest_pdf_link)
            extracted_text = extract_text_from_first_page(pdf_bytes)
        else:
            logger.warning("No PDF link found.")
            return
        
        # Extracted text is split into lines
        extracted_lines = extracted_text.split('\n')

        # Check if metadata line exists
        if find_line_with_metadata(extracted_lines, metadata_line1):
            logger.info(">>>> Metadata line found. Proceeding with data processing... <<<<")
            
            # Get patterns
            category_pattern, item_pattern = get_patterns()

            # Parse text to lists
            dates, categories, items, pettah_price_ranges, pettah_averages = parse_text(extracted_lines, category_pattern, item_pattern)

            # Convert lists to DataFrame
            list_to_dataframe = create_dataframe(dates, categories, items, pettah_price_ranges, pettah_averages)

            # Transform DataFrame
            transformed_dataframe = transform_dataframe(list_to_dataframe)

            logger.info(">>>> Data transformation completed <<<<")

            # Convert DataFrame to CSV string
            csv_data, actual_date_str = dataframe_to_csv_string(transformed_dataframe)

            # Upload CSV data to blob
            upload_to_blob(csv_data, actual_date_str)
            logger.info(">>>> CSV data uploaded to blob storage <<<<")

            # Convert DataFrame to Cosmos DB format
            cosmos_db_data = convert_dataframe_to_cosmos_format(transformed_dataframe)

            # Write Cosmos DB data
            await write_harti_data_to_cosmosdb(cosmos_db_data)
            logger.info(">>>> Completion of data ingestion to CosmosDB <<<<")

        else:
            logger.warning("Metadata line not found. Exiting without further processing.")

    except Exception as e:
        logger.error(f"Error in main execution: {e}")
        raise

def run_main():
    
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

if __name__ == '__main__':
    run_main()
