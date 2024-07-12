# text_to_dataframe.py
import re

def get_patterns():
    category_pattern = re.compile(r'^(Rice \(Rs/kg\)|Dried Chillies \(Rs/Kg\)|Onion \(Rs/Kg\)|Big Onion|Potatoes \(Rs/Kg\)|Pulses \(Rs/Kg\)|Consumption Item\(Rs/Kg\)|Eggs \(Rs/Egg\))')
    item_pattern = re.compile(r'^([a-zA-Z\s\(\)]*\d*)\s(\d+\.\d{2}\s-\s\d+\.\d{2})\s(\d+\.\d{2})')
    return category_pattern, item_pattern

def extract_date(lines):
    date_line = lines[4]
    date_match = re.search(r'\d{4}\.\d{2}\.\d{2}', date_line)
    if date_match:
        return date_match.group(0)
    return None

def parse_text(lines, category_pattern, item_pattern):
    dates = []
    categories = []
    items = []
    pettah_price_ranges = []
    pettah_averages = []

    current_category = None
    date = extract_date(lines)

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        category_match = category_pattern.match(line)
        if category_match:
            current_category = category_match.group(0)
            continue
        
        item_match = item_pattern.match(line)
        if item_match:
            item = item_match.group(1).strip()
            pettah_price_range = item_match.group(2)
            pettah_average = item_match.group(3)
            
            dates.append(date)
            categories.append(current_category)
            items.append(item)
            pettah_price_ranges.append(pettah_price_range)
            pettah_averages.append(pettah_average)
    
    return dates, categories, items, pettah_price_ranges, pettah_averages

