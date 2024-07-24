import csv
import unicodedata
from datetime import datetime

def clean_string(s):
    # Normalize to NFKD form and remove non-printable characters
    normalized = unicodedata.normalize('NFKD', s)
    cleaned = ''.join(ch for ch in normalized if unicodedata.category(ch)[0] != 'C')
    # Replace any remaining problematic characters with a space
    return ''.join(ch if ord(ch) < 128 else ' ' for ch in cleaned)

def csv_to_insert_statements(csv_file, table_name, output_file):
    with open(output_file, 'w', encoding='utf-8') as out_file:
        with open(csv_file, 'r', encoding='utf-8') as in_file:
            csv_reader = csv.DictReader(in_file)
            
            for row in csv_reader:
                columns = []
                values = []
                
                for column, value in row.items():
                    columns.append(column)

                    # Remove newlines and carriage returns from the value
                    value = clean_string(value)
                    value = value.replace('\n', ' ').replace('\r', '').strip()
                    
                    if value == '':
                        values.append('NULL')
                    # Netflix Column Adjustments
                    #elif column == 'date_added':
                    #    try:
                            # date = datetime.strptime(value, '%B %d, %Y') # This was used for the Netflix dataset
                            #values.append(f"'{date.strftime('%Y-%m-%d')}'")
                    #    except ValueError:
                    #        values.append('NULL')

                    # Video Games Column Adjustments
                    elif column == 'Year':
                        if value == 'N/A':
                            values.append('NULL')
                        else:
                            values.append(value)

                    # Escape single quotes and wrap value in single quotes
                    else:
                        values.append("'" + value.replace("'", "''") + "'")
                
                insert_statement = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(values)});\n"
                out_file.write(insert_statement)

    print(f"INSERT statements have been written to {output_file}")

# Netflix
#csv_file = 'netflix_titles.csv'  # Replace with your CSV file path
#table_name = 'shows'  # Replace with your desired table name
#output_file = 'NetflixShowsScript.sql'  # Replace with your desired output file name

# Video Games
#csv_file = 'vgsales.csv'  # Replace with your CSV file path
#table_name = 'games'  # Replace with your desired table name
#output_file = 'VideoGameScript.sql'  # Replace with your desired output file name

csv_to_insert_statements(csv_file, table_name, output_file)